pipeline{
	agent any
	
	stages{
		stage('checkout'){
			steps{
			git 'https://github.com/sarath143/jenkins-example.git'
			}
		}
		stage('Prime Series'){
			steps{	
				echo 'prime series started...'
				bat label: 'Prime series num', script: 'python -u primenumber_series.py %input_number%'
			}
		}		
	}
}
pipeline{
	agent any
	
	stages{
		stage('checkout'){
			steps{
			git 'https://github.com/sarath143/jenkins-example.git'
			}
		}
		stage('Number series'){
			parallel {
				stage('Fibnocee Series'){
					steps{	
						echo 'fibo series started...'
						bat label: 'fibo series num', script: 'python -u fibonacci_series.py %input_number%'
					}
				}
				stage('Factorial Series'){
					steps{	
						echo 'facrorial series started...'
						bat label: 'fact series num', script: 'python -u factorial_series.py %input_number%'
					}
				}
				
			}
			
		}
	}
}

