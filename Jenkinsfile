pipeline {
    agent any
    environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-credential')
	}
    stages {
        stage('Build docker image') {
            steps {
                sh 'sudo docker container prune -f'
                sh 'sudo docker build . -t dasponuku02/c270_assignment'
            }
        }

        stage('Run docker image') {
            steps {
                sh 'sudo docker run -d -p 8000:8000 -d dasponuku02/c270_assignment'
            }
        }

        stage('Login/push dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'sudo docker push dasponuku02/c270_assignment'
            }
        }
    }
    post {
		always {
			sh 'sudo docker logout'
		}
	}
}
