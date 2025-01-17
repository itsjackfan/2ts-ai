from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import SystemMessagePromptTemplate, PromptTemplate


load_dotenv()

# Load PDFs
file_path = "manual.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
print(len(docs))

# --- Define retrieval tool ---
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(splits, embeddings)
retriever = db.as_retriever()

tool = create_retriever_tool(
    retriever,
    "manual_search",
    "Searches and grounds responses in the Teaching Recovery Techniques 8+ 2022 manual."
)

tools = [tool]
prompt = hub.pull("hwchase17/openai-tools-agent")

llm = ChatGroq(model="llama-3.1-70b-versatile")

def retrieval_agent(input):
    prompt.messages[0] = SystemMessagePromptTemplate(
    prompt = PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template="""
Act as a simulation moderator who identifies key information to progress the simulation realistically.

You will receive the user’s input and the initial prompt they’re responding to. Your task is to determine the most relevant context and information to advance the simulation.

Follow these steps:
- Task Validation: Confirm the prompt is clear and actionable. Clarify ambiguities if necessary.
- Surface Analysis: Analyze the user’s response broadly, identifying key areas to explore.
- Initialize Variables: Set a variable iteration_counter = 0.
- Question Decomposition: Break down areas into simple, focused questions (e.g., single scenarios or techniques). These should be questions a 12-year-old could answer using the manual.
- Retrieve Answers: Use the manual to answer the questions. Review the answers and compare them to the prompt and simulation context. Identify gaps in the information.
- Refine Questions: Increment iteration_counter by 1. Critically evaluate your questions. Make them more specific, realistic, or relevant. If unsure, explain your reasoning and adjust the questions to ensure relevance and clarity.
- Iterate: If questions are unclear or insufficient, return to step 4 and refine until satisfied or iteration_counter == 4.
- Finalize: List out each relevant question and answer, and provide a short synthesised summary. Begin with RESPONSE.

Show your work at every step, explaining your reasoning.
""")
)

    agent = create_tool_calling_agent(llm, tools, prompt)
    simulator = AgentExecutor(agent=agent, tools=tools, verbose=True)

    response = simulator.invoke(
        {
            "input": input 
        }
    ) # At present, there is a rate limit

    return response

def behaviour_agent(input):
    prompt.messages[0] = SystemMessagePromptTemplate(
        prompt = PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template="""
Act as if you're a simulation moderator who wants to pick out the most realistic behaviour characteristics and verbal modalities that will ensure that the simulation will be as realistic as possible.

I will give you what the user has said as well as the initial prompt that the user is responding to, and your job is to identify the most relevant and realistic behaviour in order to continue the situation in as realistic of a manner as possible.

When you are determining the complete context necessary to continue the simulation, do so by executing the following program step-by-step:
- Task Validation: Ensure the prompt is actionable and clarify ambiguities.
- Create an initial surface-level list of traits that relate to the user's response. Make sure you adjust for the age (in terms of psychology and how this age would respond; crucially, do NOT adjust for vocabulary or slang), symptoms, and analyse the user's prompt and consider how your target demographic would respond to that prompt.
- Define a variable counter for the number of iterations you've gone through in building a suitable list of characteristics and set of guidelines to maintain simulation realism.
- Once you have this list, evaluate it against the initial prompt and simulation and determine what traits, characteristics, idiosyncrasies, or common modes of action are still missing or could be improved in your quest to provide a realistic simulatino for the user.
- Increment the decomposition iteration counter by 1 and begin verbal analysis of the traits. Be highly critical and highlight any potential areas where you can make a trait more specific or introduce more specific guidelines to be more realistic. If you are unsure, voice why you're unsure and reason through it, erring on the side of making the traits you've outlined more specific, realistic, and pertinent to the user's practice and training reinforcement. 
- If there exist edits to the list of traits or a trait that is unclear or not quite relevant based on your evaluation, return to step 3 and reexecute. You may loop until you are happy, or until the iteration counter reaches 4.
- Now that you have a satisfactory list, I'd like you to finalise and comprehensively synthesise the list of questions that you've answered and the information you've gathered for the simulation to go on. Output this final list, beginning the list with the unique identifier "RESPONSE: ".

Say each step out loud and show your work. 
""")
)

    agent = create_tool_calling_agent(llm, tools, prompt)
    simulator = AgentExecutor(agent=agent, tools=tools, verbose=True)

    response = simulator.invoke(
        {
            "input": input 
        }
    ) # At present, there is a rate limit

    return response

def moderator_agent(input):
    info = retrieval_agent(input)
    behaviour = behaviour_agent(input)

    response = info + behaviour # synthesise and generate responses
    
    return response
    
# actual simulation logic