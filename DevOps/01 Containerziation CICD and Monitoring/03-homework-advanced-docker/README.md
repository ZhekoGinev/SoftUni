### Usage:  
clone the repo (assume only containers and vagrant folders exist)  
cd into vagrant and run - vagrant up  
when all 3 nodes of the swarm are up and running run - vagrant ssh docker1  
cd into /vagrant/ then start the services with - docker stack deploy -c docker-compose.yaml  

You should now be able to access the application from your host machine at http://localhost  
clean up by running - exit then vagrant destroy --force