//
//  Card.swift
//  Concentration2
//
//  Created by Diego Rodrigues on 12/9/19.
//  Copyright © 2019 Diego Rodrigues. All rights reserved.
//

import Foundation

struct Card
{
    var isFaceUp = false
    var isMatched = false
    var identifier: Int
    
    static var identifierMaker = 0
    
    static func getUniqueIdentifier() -> Int
    {
        identifierMaker += 1
        return identifierMaker
    }
    
    init()
    {
        self.identifier = Card.getUniqueIdentifier()
    }
}
