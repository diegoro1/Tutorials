//
//  ViewController.swift
//  Concentration2
//
//  Created by Diego Rodrigues on 12/9/19.
//  Copyright © 2019 Diego Rodrigues. All rights reserved.
//

import UIKit

class ViewController: UIViewController
{
    lazy var game = Concentration(numberOfPairsOfCards: (cardButtons.count + 1) / 2)
    var theme = Int(arc4random_uniform(3))

    var flipCount = 0 { didSet{ flipCountLabel.text = "Flip Count: \(flipCount)"}}
    
    @IBAction func newGame(_ sender: UIButton)
    {
        game = Concentration(numberOfPairsOfCards: (cardButtons.count + 1) / 2)
        theme = Int(arc4random_uniform(3))
    }
    
    
    @IBOutlet weak var flipCountLabel: UILabel!
    
    @IBOutlet var cardButtons: [UIButton]!
    
    
    @IBAction func touchCard(_ sender: UIButton)
    {
        flipCount += 1
        if let cardNumber = cardButtons.firstIndex(of: sender)
        {
            game.chooseCard(at: cardNumber)
            updateViewFromModel()
        }
        else
        {
            print("Failed to find button")
        }
    }
    
    
    func updateViewFromModel()
    {
        for index in cardButtons.indices
        {
            let button = cardButtons[index]
            let card = game.cards[index]
            if card.isFaceUp
            {
                button.setTitle(emoji(for: card), for: UIControl.State.normal)
                button.backgroundColor = #colorLiteral(red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0)
            }
            else
            {
                button.setTitle("", for: UIControl.State.normal)
                button.backgroundColor = card.isMatched ? #colorLiteral(red: 1, green: 1, blue: 1, alpha: 0) : #colorLiteral(red: 1, green: 0.5781051517, blue: 0, alpha: 1)
            }
        }
    }
    
    
    func gameThemeSetter(themeIndex: Int) -> Array<String>
    {
        switch themeIndex
        {
        case 0:
            let theme1 = ["👻","🎃","🙀","🦇","🍬","🧙‍♂️","🦉"]
            return theme1
        case 1:
            let theme2 = ["🐶","🐱","🐭","🐹","🐰","🦊","🐻"]
            return theme2
        case 2:
            let theme3 = ["🍏","🍎","🍐","🍊","🍋","🍌","🍉"]
            return theme3
        default:
            let theme = ["","","","","","",""]
            return theme
        }
    }
    
    lazy var emojiChoices = gameThemeSetter(themeIndex: theme)
    
    var emoji = [Int:String]()
    
    func emoji(for card: Card) -> String
    {
        if emoji[card.identifier] == nil, emojiChoices.count > 0
        {
            let randomIndex = Int(arc4random_uniform(UInt32(emojiChoices.count)))
            emoji[card.identifier] = emojiChoices.remove(at: randomIndex)
            
        }
        return emoji[card.identifier] ?? "?"
    }
    
    
}

