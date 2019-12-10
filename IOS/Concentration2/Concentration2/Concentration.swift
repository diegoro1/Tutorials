//
//  Concentration.swift
//  Concentration2
//
//  Created by Diego Rodrigues on 12/9/19.
//  Copyright © 2019 Diego Rodrigues. All rights reserved.
//

import Foundation

class Concentration
{
    var cards = [Card]()
    
    func chooseCard(at index: Int)
    {
        if cards[index].isFaceUp
        {
            cards[index].isFaceUp = false
        }
        else
        {
            cards[index].isFaceUp = true
        }
    }
    
    init(numberOfPairsOfCards: Int)
    {
         for _ in 1...numberOfPairsOfCards
         {
            let card = Card()
            cards += [card, card]
         }
        // TODO:Suffle the cards
    }
}
