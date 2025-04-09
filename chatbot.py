import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration des clés API depuis les variables d'environnement
DEEPINFRA_API_KEY = os.getenv("DEEPINFRA_API_KEY")
DEEPINFRA_BASE_URL = os.getenv("DEEPINFRA_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

# Vérification de la présence des clés API
if not DEEPINFRA_API_KEY:
    st.error("Clé API DeepInfra non trouvée. Veuillez définir la variable d'environnement DEEPINFRA_API_KEY.")
    st.stop()
if not DEEPINFRA_BASE_URL:
    st.error("URL de base DeepInfra non trouvée. Veuillez définir la variable d'environnement DEEPINFRA_BASE_URL.")
    st.stop()
if not MODEL_NAME:
    st.error("Nom du modèle non trouvé. Veuillez définir la variable d'environnement MODEL_NAME.")
    st.stop()

# Initialisation du client OpenAI avec DeepInfra
openai_client = OpenAI(
    api_key=DEEPINFRA_API_KEY,
    base_url=DEEPINFRA_BASE_URL,
)

def generate_response(prompt):
    """Fonction pour générer la réponse avec l'API OpenAI via DeepInfra"""
    try:
        chat_completion = openai_client.chat.completions.create(
            model=MODEL_NAME,
            messages=st.session_state.messages,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Erreur lors de la génération de la réponse : {e}")
        return None

# Configuration de l'interface Streamlit
st.title("🤖 Chatbot avec DeepInfra")

# Initialisation de l'historique des messages dans la session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Répondez comme un assistant conversationnel."}
    ]

# Affichage de l'historique des messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Zone de saisie pour l'utilisateur
if prompt := st.chat_input("Que voulez-vous demander ?"):
    # Ajout du message de l'utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Affichage du message de l'utilisateur
    with st.chat_message("user"):
        st.markdown(prompt)

    # Génération et affichage de la réponse de l'assistant
    with st.chat_message("assistant"):
        with st.spinner("Génération de la réponse..."):
            response = generate_response(prompt)
            if response:
                st.markdown(response)
                # Ajout de la réponse de l'assistant à l'historique
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error("La génération de la réponse a échoué.")
