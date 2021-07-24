using System;
using System.IO;
using System.Diagnostics;

namespace pointathon {
    class Program {
        static void Main(string[] args) {
            var type = (SupportType) int.Parse(GetParameter(args, 0));
            var amount = int.Parse(GetParameter(args, 1));
            var subTier = GetParameter(args, 2);

            var pointsToAdd = 0;
            var multipleAmount = 1;

            switch (type) {
                case SupportType.sub:
                    multipleAmount = CalculateTypeAmount(subTier);
                    pointsToAdd = 1 * multipleAmount;
                    break;
                case SupportType.giftSub:
                    multipleAmount = CalculateTypeAmount(subTier);
                    pointsToAdd = amount * multipleAmount;
                    break;
                case SupportType.cheer:
                    pointsToAdd = amount / 500;
                    break;
            }

            var filePath = Path.GetDirectoryName(Process.GetCurrentProcess().MainModule.FileName) + "/data/points.txt";

            // Read File
            var fileData = File.ReadAllText(filePath);
            var currentCount = int.Parse(fileData);
            Console.WriteLine(currentCount);

            // Set file
            File.WriteAllText(filePath, (currentCount + pointsToAdd).ToString());
        }

        private static string GetParameter(string[] args, int parameterToGet) {
            if (args.Length >= parameterToGet + 1) {
                return args[parameterToGet];
            }
            else {
                return null;
            }
        }

        private static int CalculateTypeAmount(string subTier) {
            var multipleAmount = 1;

            if (subTier.ToLower() == "tier 1") 
            {
                multipleAmount = 1;
            }
            if (subTier.ToLower() == "tier 2") 
            {
                multipleAmount = 2;
            }
            if (subTier.ToLower() == "tier 3") 
            {
                multipleAmount = 5;
            }

            return multipleAmount;
        }
    }

    enum SupportType {
        sub = 1,
        giftSub = 2,
        cheer = 3
    }
}
