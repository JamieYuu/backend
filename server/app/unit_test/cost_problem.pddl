(define (problem grid-20)
(:domain grid-visit-all)
(:objects 
	
 loc1_1 loc1_2 loc2_1 loc2_2 - place 
        
)
(:init
	(at-robot loc1_1)
	(visited loc1_1)
	
    (connected loc1_1 loc2_1)
    (connected loc2_1 loc1_1)
    (connected loc1_1 loc1_2)
    (connected loc1_2 loc1_1)
    (connected loc1_2 loc2_2)
    (connected loc2_2 loc1_2)
    (connected loc1_2 loc1_1)
    (connected loc1_1 loc1_2)
    (connected loc2_1 loc1_1)
    (connected loc1_1 loc2_1)
    (connected loc2_1 loc2_2)
    (connected loc2_2 loc2_1)
    (connected loc2_2 loc1_2)
    (connected loc1_2 loc2_2)
    (connected loc2_2 loc2_1)
    (connected loc2_1 loc2_2)
    
    ( = (traverse-cost loc1_1 loc2_1) 1)
    ( = (traverse-cost loc2_1 loc1_1) 5)
    ( = (traverse-cost loc1_1 loc1_2) 1)
    ( = (traverse-cost loc1_2 loc1_1) 5)
    ( = (traverse-cost loc1_2 loc2_2) 1)
    ( = (traverse-cost loc2_2 loc1_2) 5)
    ( = (traverse-cost loc1_2 loc1_1) 1)
    ( = (traverse-cost loc1_1 loc1_2) 5)
    ( = (traverse-cost loc2_1 loc1_1) 1)
    ( = (traverse-cost loc1_1 loc2_1) 5)
    ( = (traverse-cost loc2_1 loc2_2) 1)
    ( = (traverse-cost loc2_2 loc2_1) 5)
    ( = (traverse-cost loc2_2 loc1_2) 1)
    ( = (traverse-cost loc1_2 loc2_2) 5)
    ( = (traverse-cost loc2_2 loc2_1) 1)
    ( = (traverse-cost loc2_1 loc2_2) 5)
    
    
    (= (total-cost) 0)

)
(:goal
    (and 
    	(visited loc2_2)
    )
) 

(:metric minimize (total-cost))

)
