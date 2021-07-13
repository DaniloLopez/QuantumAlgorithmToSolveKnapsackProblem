#!/usr/bin/env python3
# coding=utf-8

from algorithms.metaheuristics import Metaheuristic


class PsoSolution(Solution):
    def __init__(self):
        """PSO_Solution"""

    
        
"""
    


    using System;
using System.Collections.Generic;

namespace BinaryKnapsack.Algorithms.Metaheuristics.Population_based.Swarm_based
{
    public class PSOSolution:Solution
    {
        public double[] Velocity;
        public int[] BestPosition;
        public double BestFitness;

        public PSOSolution(Algorithm dueño) : base(dueño)
        {
            Velocity = new double[MyContainer.MyKnapsack.TotalItems];
            BestPosition = new int[MyContainer.MyKnapsack.TotalItems];
        }

        public PSOSolution(PSOSolution original) : base(original)
        {
            Velocity = new double[MyContainer.MyKnapsack.TotalItems];
            for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
                Velocity[d] = original.Velocity[d];
            BestPosition = new int[MyContainer.MyKnapsack.TotalItems];
            for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
                BestPosition[d] = original.BestPosition[d];
            BestFitness = original.BestFitness;
        }

        public new void RandomInitialization()
        {
            var selected = new List<int>();
            var unselected = new List<int>();

            DefineSelectedAndUnselectedLists(selected, unselected, out var myWeight);
            Complete(unselected, ref myWeight);
            Evaluate();

            BestPosition = new int[MyContainer.MyKnapsack.TotalItems];
            for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
                BestPosition[d] = Position[d];
            BestFitness = Fitness;

            Velocity = new double[MyContainer.MyKnapsack.TotalItems];
            for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
                Velocity[d] = -4 + 8 * MyContainer.MyAleatory.NextDouble();
        }

        public void UpdateVelocity(PSOSolution best)
        {
            for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
            {
                var w = MyContainer.MyAleatory.NextDouble() * ((PSO) MyContainer).W;
                var c1 = MyContainer.MyAleatory.NextDouble() * ((PSO) MyContainer).C1;
                var c2 = MyContainer.MyAleatory.NextDouble() * ((PSO) MyContainer).C2;

                Velocity[d] = w * Velocity[d] +
                              c1* (BestPosition[d] - Position[d]) +
                              c2 * (best.Position[d] - Position[d]);

                if (Velocity[d] < -4) Velocity[d] = -4;
                if (Velocity[d] > 4) Velocity[d] = 4;
            }
        }

        public void UpdatePosition()
        {
            for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
            {
                var probability = 1.0 / (1.0 + Math.Exp(-Velocity[d]));

                if (MyContainer.MyAleatory.NextDouble() < probability)
                    Position[d] = 1;
                else
                    Position[d] = 0;
            }

            var selected = new List<int>();
            var unselected = new List<int>();
            DefineSelectedAndUnselectedLists(selected, unselected, out var myWeight);
            Repare(selected, ref myWeight);
            Complete(unselected, ref myWeight);
            Evaluate();

            if (Fitness > BestFitness)
            {
                for (var d = 0; d < MyContainer.MyKnapsack.TotalItems; d++)
                    BestPosition[d] = Position[d];
                BestFitness = Fitness;
            }
        }

        public void Repare(List<int> selected, ref double myWeight)
        {
            while (myWeight > MyContainer.MyKnapsack.Capacity)
            {
                var pos = MyContainer.MyAleatory.Next(selected.Count);
                var posTurnOff = selected[pos];
                selected.RemoveAt(pos);
                Position[posTurnOff] = 0;
                myWeight -= MyContainer.MyKnapsack.Weight(posTurnOff);
            }
        }
    }
}



"""
        
