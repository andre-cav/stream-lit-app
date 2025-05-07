
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
    {"nome": "Análise de clientes com SQL e Python", "link": "https://github.com/andre-cav/Customer-Analytics-with-SQL-and-Python"},
    {"nome": "Análise de ações com Python", "link": "https://github.com/andre-cav/Python-For-Finance"},
    {"nome": "Diversas análises na área do futebol", "link": "https://github.com/andre-cav/Python-For-Soccer"},
    {"nome": "Análise usando LGBM model", "link": "https://github.com/andre-cav/Credit-Risk-with-Python/blob/main/Heart_Attack_Prediction.ipynb"}
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
