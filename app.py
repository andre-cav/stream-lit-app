
import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="André Cavalcanti",
    page_icon=":briefcase:",
    layout="wide",
)

# --- Seção de Apresentação ---
st.title("André Cavalcanti - Portfolio :rocket:")
st.subheader("Aqui você encontrará alguns dos meus projetos.")
st.write("Meu nome é André Cavalcanti, sou formado em Engenharia de Produção pela Universidade Federal Fluminense e no momento estou cursando Master in Data Science pela FGV.")
st.write("Estou há alguns anos trabalhando na área de dados. Comecei como planner na Duty Free Dufry, passei pela área de seguros na Mag Seguros e atualmente estou na JHSF.")
st.markdown("---")

# --- Seção de Projetos ---
st.header("Meus Projetos")

# Lista de projetos com nome e link
projetos = [
    {"nome": "Projeto de Análise de Dados", "link": "https://link_para_seu_projeto_1.com"},
    {"nome": "Aplicação Web com Streamlit", "link": "https://link_para_seu_projeto_2.com"},
    {"nome": "Repositório de Machine Learning", "link": "https://link_para_seu_projeto_3.com"},
    {"nome": "Outro Projeto Interessante", "link": "https://link_para_seu_projeto_4.com"},
]

# Exibição dos projetos como links em Markdown
for projeto in projetos:
    markdown_link = f"[{projeto['nome']}]({projeto['link']})"
    st.markdown(f"- {markdown_link}")

st.markdown("---")

# --- Seção de Contato (Opcional) ---
st.header("Entre em Contato")
st.write("Se você tiver alguma dúvida ou quiser conversar sobre algum projeto, fique à vontade para me contactar!")
st.write(":email: andregomespc@gmail.com")
st.write(":linkedin: [Meu LinkedIn](https://www.linkedin.com/in/andr%C3%A9-cavalcanti-591998106/)")
st.write(":github: [Meu GitHub](https://github.com/andre-cav)")

# --- Rodapé ---
st.markdown("---")
st.write("André Cavalcanti")
