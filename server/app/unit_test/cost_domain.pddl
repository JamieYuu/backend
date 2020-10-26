(define (domain grid-visit-all)
(:requirements :typing :action-costs)
(:types        place - object)
(:predicates
	     (connected ?x ?y - place)
	     (at-robot ?x - place)
	     (visited ?x - place)
)
	
(:functions 
    (total-cost)
    (traverse-cost ?x ?y - place)
)
	
(:action move
:parameters (?curpos ?nextpos - place)
:precondition (and (at-robot ?curpos) (connected ?curpos ?nextpos))
:effect (and (at-robot ?nextpos) (not (at-robot ?curpos)) (visited ?nextpos)
        (increase (total-cost) (traverse-cost ?curpos ?nextpos))
        )
)

)

