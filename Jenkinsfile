pipeline {
  agent any
    stages {
      stage('git_pull') {
        steps {
           bat 'git pull https://github.com/Adarbe/FinalProject.git'
        }
      }
      stage('run_docker') {
        steps {
          bat 'docker-compose up -d'
        }
      }
      stage('run_redisapp') {
        steps {
          sh 'redisapp.py'
        }
      }
      }
      
    post {
      always {
        bat "echo end"
      }
    }
}
