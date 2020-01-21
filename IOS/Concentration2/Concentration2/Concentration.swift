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
    
    var indexOfOneAndOnlyFacedUpCard: Int?
    
    func chooseCard(at index: Int)
    {
        if !cards[index].isMatched
        {
            if let matchIndex = indexOfOneAndOnlyFacedUpCard, matchIndex != index
            {
                if cards[matchIndex].identifier == cards[index].identifier
                {
                    cards[matchIndex].isMatched = true
                    cards[index].isMatched = true
                }
                cards[index].isFaceUp = true
                indexOfOneAndOnlyFacedUpCard = nil
            }
            else
            {
                for flipDownIndex in cards.indices
                {
                    cards[flipDownIndex].isFaceUp = false
                }
                cards[index].isFaceUp = true
                indexOfOneAndOnlyFacedUpCard = index
            }
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
