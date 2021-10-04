# -*- coding: utf-8 -*-
#!/usr/bin/python


from algorithms.metaheuristics import Metaheuristic

class Pso(Metaheuristic):

    def __init__(self, max_efos):
        super().__init__(max_efos)
        self.swarm_size = 50
        self.W = 1;  #alpha - momentum
        self.C1 = 1;  #beta - cognitive component
        self.C2 = 1;  #delta - social component
        self.E = 1;  #epsilon (velocity consideration)
        

    def execute(self, theKnapsack, theAleatory):
        pass


    """
        CurrentEFOs = 0;
        Curve = []
        
        #revisar declaracion de esta variable 
        swarm = []<PSOSolution>;
        
        for i in range(1,self.swarm_size):            
            var newParticle = new PSOSolution(this);
            newParticle.RandomInitialization();
            swarm.Add(newParticle);
            if (Math.Abs(newParticle.Fitness - MyKnapsack.OptimalKnown) < 1e-10)
                break;

    continuar revisando
        var maxFitness = swarm.Max(x => x.Fitness);
        var best = swarm.Find(x => Math.Abs(x.Fitness - maxFitness) < 1e-10);
        MyBestSolution = new PSOSolution(best);

        while (CurrentEFOs < MaxEFOs && Math.Abs(MyBestSolution.Fitness - MyKnapsack.OptimalKnown) > 1e-10)
        {
            for (var i = 0; i < SwarmSize; i++)
                swarm[i].UpdateVelocity((PSOSolution)MyBestSolution);

            for (var i = 0; i < SwarmSize; i++)
            {
                swarm[i].UpdatePosition();
                if (Math.Abs(swarm[i].Fitness - MyKnapsack.OptimalKnown) < 1e-10)
                    break;
            }

            maxFitness = swarm.Max(x => x.Fitness);
            best = swarm.Find(x => Math.Abs(x.Fitness - maxFitness) < 1e-10);
            if (maxFitness > MyBestSolution.Fitness)
                MyBestSolution = new PSOSolution(best);
        }
        """