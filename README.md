# Interview Trainer Agent using IBM Watsonx AI

## Problem Statement

Interview Trainer Agent

## Project Description

Interview Trainer Agent is an AI-powered interview preparation assistant built using IBM Watsonx AI, LangFlow, Python and Streamlit.

The application helps users prepare for interviews by generating personalized interview questions based on uploaded resumes and selected job roles.

If a resume is uploaded, the AI generates questions from the candidate's skills, projects and technologies. If no resume is uploaded, the AI generates role-based interview questions.

## Features

* Resume Upload (PDF/TXT)
* Personalized Interview Questions
* Role-Based Question Generation
* Beginner, Intermediate and Advanced Levels
* IBM Watsonx AI Integration
* LangFlow Workflow
* Interactive Streamlit Interface

## Technology Stack

* Python
* Streamlit
* IBM Watsonx AI
* LangFlow
* IBM Cloud
* PDF Processing

## Architecture

User → Resume Upload → Streamlit UI → LangFlow Workflow → IBM Watsonx AI → Foundation Model → Interview Questions

## Installation

Install dependencies:

pip install -r requirements.txt

## Run Project

streamlit run app.py

## Expected Output

* Upload Resume
* Select Target Role
* Generate Personalized Interview Questions
* AI returns interview preparation questions

## Future Enhancements

* Mock Interview
* AI Evaluation
* Interview Scorecard
* Resume Analysis
* Career Recommendations
