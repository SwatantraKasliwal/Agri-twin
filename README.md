# 🌾 Agri-Twin

**Agri-Twin** is an **AI-powered digital twin for precision agriculture** that helps farmers make **smarter irrigation and fertilization decisions** using **reinforcement learning (RL)** and environmental simulation.

The system models a virtual version of a farm, continuously learns optimal irrigation strategies, and provides **explainable recommendations** that balance **crop health, water efficiency, and environmental stress**.

---

## 🎯 Project Vision

Modern agriculture faces three major challenges:

1. **Water scarcity**
2. **Climate variability (heat stress, irregular rainfall)**
3. **Lack of data-driven decision support for small & medium farmers**

**Agri-Twin** addresses these challenges by combining:
- 🌱 Crop growth simulation  
- 🤖 Reinforcement learning–based decision making  
- 📊 Real-time explainable recommendations  

The goal is **not automation for automation's sake**, but **decision support that farmers can understand and trust**.

---

## 🧠 What is a Digital Twin (in simple terms)?

A **digital twin** is a **virtual copy of a real-world system**.

In Agri-Twin:
- The **farm** is digitally recreated
- Weather, soil moisture, heat stress, and crop growth are simulated
- An AI agent learns by interacting with this virtual farm
- The learning is then used to **recommend actions in the real world**

Think of it as:
> "A safe virtual farm where AI learns what works best — before suggesting it to real farmers."

---

## 🧩 High-Level Architecture

```
Farmer / User
↓
Web Dashboard (Frontend)
↓
FastAPI Backend
↓
RL Decision Engine (PPO Agent)
↓
Crop & Environment Simulator
↓
Irrigation + Fertilizer Recommendations
```

---

## 👨‍🌾 User Perspective: How Farmers Use Agri-Twin

### 1️⃣ What the Farmer Sees

A farmer interacts with Agri-Twin through a **simple dashboard**, not code.

They can see:
- Current soil moisture
- Crop growth stage
- Heat stress levels
- Rainfall impact
- Recommended irrigation amount
- Fertilizer suggestion + reason

No ML knowledge required.

---

### 2️⃣ What the Farmer Inputs

Minimal and realistic inputs:
- Crop type (current prototype: generic crop)
- Farm location (future scope: weather-based)
- Basic soil conditions
- Start of growing season

*(In the prototype, these are simulated.)*

---

### 3️⃣ What the Farmer Understands

Each recommendation is **explainable**:

> "Soil moisture is low and crop is in vegetative stage → irrigate 15 mm today."

> "Heat stress detected during flowering → add phosphorus and potassium."

The farmer is **never asked to blindly trust the AI**.

---

### 4️⃣ What the Farmer Gains

- Reduced water waste
- Healthier crops
- Less guesswork
- Early warnings for stress
- Confidence in decisions

Agri-Twin acts as a **decision assistant**, not a replacement.

---

## 🔄 User Flow (End-to-End)

### Step 1: Start Simulation
- User opens the dashboard
- Clicks **Reset / Start Season**
- Digital farm is initialized

### Step 2: AI Observes Farm State
- Soil moisture
- Heat stress
- Rainfall
- Crop growth stage

### Step 3: AI Decides Irrigation
- RL agent predicts optimal irrigation amount
- Decision balances crop health & water efficiency

### Step 4: Fertilizer Advisory
- Rule-based logic analyzes crop stage + stress
- Suggests fertilizer type with reasoning

### Step 5: Results Displayed
- Updated farm state
- Clear explanation of decisions
- Visual trends over time

### Step 6: Repeat Daily
- System simulates day-by-day farming decisions
- Learns long-term strategies

---

## 🤖 Intelligence Behind the Scenes (Simplified)

### Reinforcement Learning (RL)
- The system uses **Proximal Policy Optimization (PPO)**
- The AI learns by:
  - Trying irrigation actions
  - Observing outcomes
  - Receiving rewards or penalties

### Reward Philosophy
- Encourage optimal soil moisture
- Penalize over- and under-irrigation
- Discourage unnecessary water usage

📌 *This is a domain-inspired learning process, not a yield prediction model.*

---

## 🏗️ Project Structure

```
Agri-Twin/
├── backend/        # RL environment, PPO agent, API
├── frontend/       # Dashboard UI (visualization & interaction)
├── models/         # Trained RL models
├── docs/           # Diagrams and explanations
└── README.md       # This file
```

---

## 🌱 Current Capabilities

- ✅ Custom crop–environment simulator
- ✅ PPO-based irrigation optimization
- ✅ Fertilizer advisory logic
- ✅ Explainable decisions
- ✅ REST API for frontend
- ✅ Interactive 3D farm visualization
- ✅ Real-time dashboard with metrics

---

## 🚀 Future Scope

- Multi-crop and crop-specific modeling
- Real weather API integration
- Scientific crop models (WOFOST)
- IoT sensor data ingestion
- Multi-farm comparisons
- Long-term seasonal learning
- Mobile-first farmer interface

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup
```bash
# Clone repository
git clone https://github.com/yourusername/Agri-twin.git
cd Agri-twin

# Create virtual environment
python -m venv env_agritwin
env_agritwin\Scripts\activate  # Windows
# source env_agritwin/bin/activate  # Linux/Mac

# Install dependencies
cd backend
pip install -r requirements.txt

# Start API server
cd ..
uvicorn backend.api.server:app --reload --port 5000
```

### Frontend Setup
```bash
# In a new terminal
cd frontend
npm install
npm run dev
```

Access the dashboard at: `http://localhost:5173`

---

## ⚠️ Disclaimer

⚠️ **Agri-Twin is a research and educational prototype.**  
It is not intended to replace certified agronomic advice or real-world agricultural expertise.

---

## 🧑‍💻 Who This Project Is For

- 🌾 Farmers seeking decision support
- 🎓 Students learning RL + simulation
- 🧠 Researchers in digital twins
- 🌍 Climate-tech innovators
- 🏆 Hackathon judges & evaluators

---

## 📂 Additional Documentation

- [Backend README](backend/README.md) - Detailed technical documentation
- [Frontend Documentation](frontend/README.md) - UI component guide
- [API Reference](backend/api/README.md) - Endpoint documentation

---

## 📝 License & Authors

- **Team:** Byte


---

## 🙌 Final Note

Agri-Twin is built with the belief that **AI should explain itself**,  
**technology should empower farmers**,  
and **sustainability should be measurable, not assumed**.