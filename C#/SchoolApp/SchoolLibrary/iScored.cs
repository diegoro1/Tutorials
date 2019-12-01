using System;
namespace SchoolLibrary
{
    public interface IScored
    {
        float Score { get; set; } // unlike java!
        float MaxScorer { get; set; }
    }
}
