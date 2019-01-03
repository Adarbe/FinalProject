pipeline {
  agent any
    stages {
      stage('start') {
        steps {
          bat 'echo "Hello World"'
        }
      }
    }
    post {
      always {
        bat "echo end"
      }
    }




}
