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
               echo 'installing dependencies...'
                
            }
        }
        
        stage('Run Tests') {
            steps {
                script{
                sh 'python3 test_file.py'
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
