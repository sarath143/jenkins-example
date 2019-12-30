pipeline{
	agent any
	
	stages{
		stage('checkout'){
			git checkout
		}
		stage('Run primenumber series'){
			steps{
				echo "Generating primber number"
				timeout(time:3, unit:MINUTE){
					python primenumber_series 10
				}
			}
		}
		stage('Run fibonaciee series'){
			steps{
				echo "Generating primber number"
				timeout(time:3, unit:MINUTE){
					python fibonacci_series 10
				}
			}
		}
		
		stage('Run factorial series'){
			steps{
				echo "Generating primber number"
				timeout(time:3, unit:MINUTE){
					python factorial_series 10
				}
			}
		}
		
			
	}
}
