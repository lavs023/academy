pipeline {
  agent none
  stages {
    stage('deploy') {
      steps {
        sh 'ls >> test'
      }
    }
  }
  environment {
    test = ''
  }
}