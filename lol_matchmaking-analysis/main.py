from riot_api impot get_match_data
from analysis import analyze

def main():
    data = get_match_data()
    result = analyze(data)
    print(result)

if __name__ == "__main__":
    main()