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
