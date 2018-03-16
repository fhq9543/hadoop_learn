import csv
import sys

def load_country_medals(country_files):
    countries = {}
    try:
        # Read table - medal|prize|country|year
        with open(country_files) as f:
            reader = csv.reader(f, delimiter='|', quotechar='"', doublequote=False)
            reader.next()
            for line in reader:
                countries[(line[2], line[3], line[0])] = line[1]

    except:
        pass

    return countries

def read_input(file):
    file.next()
    for line in file:
        yield line.rstrip().split('|')

def main():
    medal_price = load_country_medals('./CountryMedals.txt')
    data = read_input(sys.stdin)
    total_price = 0
    for athlete, age, country, year, ceremony, sport, gold, silver, bronze, total in data:
        int(total)

        if gold > 0 and (country, year, 'Gold') in medal_price:
            total_price += int(medal_price[(country, year, 'Gold')]) * int(gold)

        if silver > 0 and (country, year, 'Silver') in medal_price:
            total_price += int(medal_price[(country, year, 'Silver')]) * int(silver)

        if bronze > 0 and (country, year, 'Bronze') in medal_price:
            total_price += int(medal_price[(country, year, 'Bronze')]) * int(bronze)

        print '%s,%s,%s,%s,%s' % (athlete, sport, country,total, total_price)


if __name__ == '__main__':
    main()
