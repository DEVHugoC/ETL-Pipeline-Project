	pipeline {
	  agent any
	  stages {
	    stage('Actualizar código') {
	      steps {
	        git branch: 'main', url: 'https://github.com/DEVHugoC/ETL-Pipeline-F-.git'
	      }
	    }
	    stage('Ejecutar ETL') {
	      steps {
	        sh '''
	          cd /var/jenkins_home/PROY_PY_CERTUS
	          if [ ! -d venv ]; then
	            python3 -m venv venv
	            . venv/bin/activate
	            pip install pandas seaborn matplotlib openpyxl
	          else
	            . venv/bin/activate
	          fi
	          python3 Proceso.py
	        '''
	      }
	    }
	  }
	  post {
	    success { echo 'ETL completado.' }
	    failure { echo 'Error en ETL.' }
	  }
	}
