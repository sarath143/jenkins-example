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
			
			bat label: 'Prime series numbers', script: 'C:/Users/C52816A/AppData/Local/Programs/Python/Python37/python.exe python primenumber_series.py 10'
			}
		}
	}
}
