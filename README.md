
# Brittenwoods Gold – Global Visa Remittance Platform

## App Features
- Black + Gold UI
- Secure card issuance and activation
- Employer payroll disbursement via paystub PIN
- ATM withdrawal with dynamic or sender-linked PINs
- Transfer Tree enforcement: 15 (Individual), 25 (SME)

## Project Structure
- /frontend → React Native mobile app
- /backend → FastAPI services
- /docs → Compliance policies
- /designs → UI mockups

## Run Instructions
Frontend:
  cd frontend && npm install && npm start

Backend:
  cd backend && uvicorn main:app --reload
