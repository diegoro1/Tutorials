//
//  ViewController.swift
//  Concentration
//
//  Created by Diego Rodrigues on 12/7/19.
//  Copyright © 2019 Diego Rodrigues. All rights reserved.
//

import UIKit

class ViewController: UIViewController
{
    var flipCount = 0
    {
        didSet
        {
            flipCountLabel.text = "Flips: \(flipCount)"
        }
    }
    
    @IBOutlet var cardButtons: [UIButton]!
    
    @IBOutlet weak var flipCountLabel: UILabel!
    
    
    @IBAction func touchCard(_ sender: UIButton)
    {
        flipCount += 1
        let cardNumber = cardButtons.lastIndex(of: sender)!
        print("cardNumber == \(cardNumber)")
    }

    
    func flipCard(withEmoji emoji: String, on button: UIButton)
    {
        if button.currentTitle == emoji
        {
            button.setTitle("", for: UIControl.State.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 0.5781051517, blue: 0, alpha: 1)
        }
        else
        {
            button.setTitle(emoji, for: UIControl.State.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
        }
    }
}
















