pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Requirements') {
            steps {
                script{
                bat 'python --version'
                bat 'pip install --user -r requirements.txt'
                bat 'pip install pytest'    
                }
                
            }
        }
        
        stage('Run Tests') {
            steps {
                script{
                bat 'python test_file.py'
                }
            }
        }
       stage("groooove"){
            steps{
                script{
                    ZZ = load 'MlOps.groovy'
                    ZZ.testfunc("Prod")
                    
                }
            }
           
       }
    }
}
