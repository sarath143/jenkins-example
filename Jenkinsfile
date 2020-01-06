pipeline{
	agent any
	
	stages{
		stage('checkout'){
			steps{
			git 'https://github.com/sarath143/jenkins-example.git'
			}
		}	
		stage('prime series'){
			steps{	
				echo 'prime series started...'
				bat label: 'Prime series num', script: 'python -u primenumber_series.py 1000'
			}
		}
	}
}
