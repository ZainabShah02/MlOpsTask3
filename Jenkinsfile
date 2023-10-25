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
                powershell 'python --version'
                powershell 'pip install --user -r requirements.txt'
                powershell 'pip install pytest'    
                }
                
            }
        }
        
        stage('Run Tests') {
            steps {
                script{
                powershell 'python test_file.py'
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
