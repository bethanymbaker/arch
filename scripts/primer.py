import json

docid_to_title = json.loads(
    '{"28099931907": {"content": {"title": "Vaccine nationalism: US says it won\'t join global effort for COVID-19 inoculation"}}, "28108959337": {"content": {"title": "What If China Gets the Covid-19 Vaccine First?"}}, "28110814722": {"content": {"title": "Canada, Two US Firms Sign COVID-19 Vaccine Deals - Trudeau"}}, "28101422554": {"content": {"title": "White House says Senate Republicans may take up COVID-19 bill next week"}}, "28099132063": {"content": {"title": "White House slams WHO over criticism of push for..."}}, "28101167069": {"content": {"title": "Advisers See No Data Favoring Trump-Touted Plasma Therapy"}}, "28102817621": {"content": {"title": "Is Covid-19 vaccine round the corner?"}}, "28108039075": {"content": {"title": "Trump Blasts Biden In Acceptance Speech, Calls Him \'Trojan Horse For Socialism\'."}}, "28098698025": {"content": {"title": "19 \'what if\' COVID-19 questions answered"}}, "28097027782": {"content": {"title": "U.S. to acquire 150 million rapid tests on Covid-19"}}, "28111131355": {"content": {"title": "Operation Warp Speed: US coronavirus vaccine research on track"}}, "28110856451": {"content": {"title": "Pelosi, White House call on COVID-19 aid ends without a breakthrough"}}, "28106625838": {"content": {"title": "CDC walks back COVID-19 testing guidelines"}}, "28099931906": {"content": {"title": "A coronavirus vaccine: China’s got one, Russia does, too. Will Trump rush one out?"}}, "28096859458": {"content": {"title": "There is a path out of America’s COVID-19 mess—if we choose to take it"}}, "28110814723": {"content": {"title": "CDC rolls out controversial new coronavirus testing guidelines as Trump aide refers to pandemic in past tense"}}, "28093906031": {"content": {"title": "Drug giant AstraZeneca starts trial of Covid-19 antibody injections"}}, "28108873175": {"content": {"title": "Data show how superspread event sent COVID-19 across nation", "sources": ["ABC", "FOX"]}}, "28103573587": {"content": {"title": "The intricate path towards a COVID-19 vaccine.(Opinion-Editorial)"}}, "28096849799": {"content": {"title": "Is a repeat coronavirus infection possible?"}}, "28098943696": {"content": {"title": "\'Warp Speed\' COVID-19 Vaccine Efforts Aim for Diverse Volunteers and Long-Lasting Protection"}}, "28110942840": {"content": {"title": "How Politics Muddied the Waters on a Promising COVID-19 Treatment"}}, "28107038234": {"content": {"title": "How Convalescent Plasma Could Help Fight COVID-19"}}, "28084509076": {"content": {"title": "Scientists to Wall Street: You don’t really understand how COVID vaccine tests work"}}, "28089633072": {"content": {"title": "Trump announces plasma treatment authorized for COVID-19"}}, "28099749478": {"content": {"title": "Trump considering fast-tracking UK COVID-19 vaccine before election - FT"}}, "28099468922": {"content": {"title": "9 reasons you can be optimistic that a vaccine for COVID-19 will be widely available in 2021"}}, "28107540657": {"content": null}, "28098940419": {"content": {"title": ""}}, "28110838282": {"content": {"title": "COVID-19 Disparities and the Black Community: A Health Equity–Informed Rapid Response Is Needed"}}, "28093943889": {"content": {"title": "AstraZeneca to transfer to Argentina the technology to produce the coronavirus vaccine"}}, "28099506681": {"content": {"title": "COVID-19 vaccine update: Fauci says won\'t make vaccination mandatory in the US"}}, "28084188573": {"content": {"title": "The CDC wants state and local sewage systems tested for coronavirus"}}, "28109130960": {"content": {"title": "Global coronavirus vaccine race: What you need to know"}}, "28097129455": {"content": {"title": "COVID-19 Update: Oleander Extract, Younger Adults"}}, "28110653655": {"content": {"title": "Scarce coronavirus vaccine should go to frontline health workers first, report suggests"}}, "28110819318": {"content": {"title": "Fact check: Fauci did not approve hydroxychloroquine as a cure for coronaviruses in 2005"}}, "28106754872": {"content": {"title": "Mink on Utah Fur Farms Test Positive for COVID-19 Virus"}}, "28093906030": {"content": {"title": "VBI Vaccines signs manufacturing deal for COVID-19 vaccine candidates"}}, "28108257314": {"content": {"title": "Regeneron, Roche team up in global deal on Covid-19 antibody cocktail"}}, "28097690131": {"content": {"title": "Australia To Be Among The First To Receive COVID-19 Vaccine From AstraZeneca"}}, "28096854777": {"content": {"title": "Gov. Andrew Cuomo book on COVID-19 response out in October"}}, "28100917473": {"content": {"title": "Yale Patents A New Saliva-Based COVID-19 Test That Is Only Worth $10!"}}, "28099198548": {"content": {"title": "Here are the most promising coronavirus vaccine candidates out there"}}, "28110814724": {"content": {"title": "Coronavirus: Infectiousness vs severity, what\'s the difference?"}}, "28110749186": {"content": {"title": "CDC says number, rate of coronavirus cases in children rising"}}, "28110001860": {"content": {"title": "J and J reaches USD 1B Covid-19 vax deal with US"}}, "28109184578": {"content": {"title": "Peter Navarro on stalled COVID-19 relief plan: Reaching a deal \'should be easy\'"}}, "28100566138": {"content": {"title": "Coronavirus updates: CDC says rate of COVID cases in children \'steadily increasing\'"}}, "28085937302": {"content": {"title": "EXCLUSIVE-U.S. to make coronavirus strain for possible human challenge trials"}}, "28108954857": {"content": {"title": "Russia has won the COVID-19 Vaccine race"}}, "28098853699": {"content": {"title": "European Commission orders AstraZeneca’s COVID-19 vaccine"}}, "28110991149": {"content": {"title": "US scientists are MAKNG a strain of coronavirus to INFECT healthy volunteers in \'challenge\' trials of vaccines against COVID-19"}}, "28098130400": {"content": {"title": "Early spread of COVID-19 far greater than initially reported: Study"}}}')

# 1. Write a function that identifies all the unique words across all the `content.title` fields in `docid_to_title`.
titles = []

for key in docid_to_title.keys():
    document = docid_to_title[key]
    try:
        title = docid_to_title[key]['content']['title']
        titles.append(title)
    except:
        pass

words = []
for title in titles:
    words.extend(title.split(' '))

lower_words = [val.lower() for val in words if val != '']
unique_words = set(lower_words)


# 2. Write a function that computes the k most frequent bigrams across all the `content.title` fields in `docid_to_title`.


def get_bigram(text):
    words = text.split(' ')
    bigrams = []
    first_word = words.pop(0)
    for idx, word in enumerate(words):
        bigram = ' '.join([first_word, word])
        first_word = word
        bigrams.append(bigram)
    return bigrams


def get_k_bigrams(titles, k):
    all_bigrams = []
    for title in titles:
        all_bigrams.extend(get_bigram(title))

    bigram_d = {}
    for bigram in all_bigrams:
        if bigram in bigram_d:
            bigram_d[bigram] += 1
        else:
            bigram_d[bigram] = 1

    sort_d = sorted(bigram_d.items(), key=lambda x: x[1], reverse=True)
    to_return = []
    for i in range(k):
        to_return.append(sort_d[i][0])
    return to_return


print(get_k_bigrams(titles, 5))

# 3. Find all the duplicate titles in `content.title` fields in `docid_to_title`.
