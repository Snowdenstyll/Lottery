# Lottery Analysis Web Application

## Overview
The Lottery Analysis Web Application is a **full-stack web application** designed for analyzing lottery numbers. It leverages modern web technologies to provide users with insights and predictions based on historical lottery data. The application features a user-friendly interface and robust backend to handle data processing and machine learning tasks.\
Visit [lottery.brandenvongphakdy.com](https://lottery.brandenvongphakdy.com/)

## Tech Stack
- Frontend: React.js
- Backend: Python Flask
- Database: SQLite
- Hosting: AWS EC2
- SSL: Let's Encrypt
- Proxy: Nginx

## Directory Structure
```
Lottery/
├── client/                 # React frontend
│   ├── build/             # Production build
│   ├── public/            # Static assets
│   ├── src/               # Source code
│   └── package.json       # Dependencies
├── server/                # Flask backend
│   ├── data/             # Lottery datasets
│   ├── database/         # SQLite models
│   ├── keras/            # ML models
│   ├── routes/           # API endpoints
│   └── requirements.txt  # Python dependencies
```

## Setup

### Local Development
```powershell
# Frontend
cd client
npm install
npm start

# Backend
cd server
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Production Deployment
```bash
# AWS EC2 Setup
sudo yum update -y
sudo yum install nginx python3.11

# SSL Certificate
sudo certbot --nginx -d lottery.brandenvongphakdy.com

# Start Services
pm2 start app.py --name "flask-api"
sudo systemctl start nginx
```

## Environment Variables
```env
FLASK_APP=app.py
FLASK_ENV=production
```

## API Endpoints
- `GET /lottery` - Retrieve lottery analysis
- `POST /lottery` - Submit new numbers

## Security
- HTTPS enabled
- Nginx reverse proxy
- AWS security groups configured
- Regular security updates

## Live Site
https://lottery.brandenvongphakdy.com

## Maintenance
- SSL auto-renewal
- Database backups
- Log rotation
- Security patches

## License
MIT

## Author
Branden Vongphakdy