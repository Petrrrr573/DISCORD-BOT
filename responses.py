import random

vtipy = ["Víte jak začíná příběh ekologů? Bio nebio...",
         "Víte, proč krab nemá peníze? Protože je na dně.",
         "Na obale salámu je napsáno: Na 100 g výrobku bylo použito 125 g masa.",
         "Pilát potká Ježíše a řekne mu: „Já jsem Pilát.“A Ježíš na to odpoví:„Pilát? Jako ten z Kalibiku?“",
         "Když cítíte bolest v noze, amputujte si ruku. Už neucítíte bolest v noze!",
         "Jaký je rozdíl mezi krávou a autobusem? Autobus má stěrače vepředu, kráva vzadu.",
         "Informatik je člověk, který vyřeší problém, který nikdy neexistoval,způsobem, kterému nikdo nerozumí.",
         "Víte, jak se říká lidem, kteří utíkají před kanibaly? Fast Food.",
         "Kdo jí hodně cibule, k tomu nechodí lékař. Kdo jí hodně česneku, k tomu nechodí nikdo.",
         "Dnes jsem si procházel staré fotky mé prababičky. Teď mi ale pořád vrtá hlavou, proč nosila jen černé a bílé oblečení...",
         "Sedí babička v parku na lavičce a modlí se: „Pane, já už jsem zase nevyšla s důchodem, pošli mi, prosím, nějak stovku.“ Zaslechne to nějaký mladý muž a říká jí: „Prosím vás, babičko, přece nebudete věřit takovým pověrám... Tady máte padesátikorunu a už se nemodlete.“ Babička chvilku počká, až se onen muž vzdálí, a pak říká: „Děkuju Ti, Pane. A příště mi to, prosím, neposílej po takovém neznabohovi, zase si půlku nechal...“",
         "Černý humor je jako dítě z Afgánistánu. Nemá hlavu, ani patu.",
         "Když někdo umře, tak o tom neví, ale pro ostatní je to těžké... To samé platí, když je někdo debil.",
         'Chlap v lese brutálně znásilní holku. Když se zvedá a zapíná si poklopec, s radostí prohlásí: "Až se to narodí, říkej tomu třeba Franta."Ona na to: "Hmm, až se to projeví, říkej tomu třeba chřipka debile."',
         'Pletou dvě nastávající maminky malé svetříky pro své ratolesti a jedna říká: "Doufám že to bude chlapeček, mám jenom modrou přízi. "Druhá říká: "Doufám že to bude kripl, zkurvila jsem rukáv."',
         'Horoskop na zítřejší den: Zítra vás budou všichni jenom chválit, budou vás na rukou nosit a zahrnovat květinami. Jóóó, pohřeb už je takovej...',
         'Jede beznohý vozíčkář po Václaváku a volá na něj vekslák: "Pane, nekoupíte si boty?" No, vozejčkář je pěkně nasranej a zavolá na nedaleko stojícího policistu: "Viděl jste to? Ten chlap mne urazil!" "Tak proč jste ho nenakopal do prdele?" na to policajt. To ubozaka dorazi. Dojede domu a stěžuje si manželce. "Nic si z toho nedělej", povídá manželka, "uvařím ti kafe, to tě postaví na nohy."',
         'Víte jaký je rozdíl mezi černým, brutálním a morbidním humorem? Černý: Deset cikánů v jedné popelnici. Brutální: Jeden cikán v deseti popelnicích. Morbidní: Deset popelnic v jednom cikánovi.',
         'Víte co znamená pro lidožrouta těhotná žena? Kinder vejce.',
         'Leží dva vandráci u kolejí, oba bez nohou. A jeden říká druhému: "Já jsem ti říkal, že sova houká jinak!"',
         'Jaký rozdíl je mezi obilím a naší vládou? Žádný. Obojí je třeba vymlátit abychom nepochcípaly hlady.',
         'Když jsem byla menší, účastnila jsem se svateb starších příbuzných. To pak za mnou vždycky chodily babičky, štípaly mě do tváře a otravovaly se slovy: "Ty budeš další.."Ale přestaly s tím, když jsem jim já to samé začala dělat na pohřbech..',
         'Fábio si hrál s míčem. Míč se však zakutálel na vozovku. Škoda Fábia....',
         'Šly děti po minovém poli a rozhazovaly rukama... některé i 30 metrů!',
         'Sedí indián u vodopádu a kouká na svou ženu jak pere prádlo. V tom z vodopádu spadne kámen jeho ženě na hlavu a zabije ji. Indián zkušeně: "To už je třetí pračka, kterou mi zničil vodní kámen."',
         'Víte, jaký je oblíbený nápoj vozíčkářů? Točená kola.',
         'Říkala, že ji rozbrečí jedině cibule. Když jsem jí hodil na hlavu meloun, tak okamžitě změnila názor.',
         'Mladík v lékárně: "Dejte mi balíček kondomů. Příchuť jahoda, anebo ne, malina. Existuje jablko? Anebo máte i banán?" Děda, který stojí ve frontě za ním: "Synku, chceš jebat, nebo vařit kompot?!"',
         'Pacient povídá doktorovi: "Až umřu, tak do úmrtní zprávy napište, že jsem umřel na AIDS". Doktor se tomu diví a povídá: "Vy nemáte AIDS, ale rakovinu". Pacient odpoví: "To nevadí, ale já k tomu mám 3 dobré důvody: Za prvé takovou nemoc u nás na vsi ještě nikdo nemá, za druhé soused umře strachy že to má taky, protože mi chodil za manželkou, a za třetí manželka si do smrti nezašuká."',
         'Do banky vběhne ozbrojený lupič v masce a zařve: "Všichni na zem! A pokladní ke mě!" Přišla vystrašená pokladní, lupič si rozepnul zip, vytáhl ptáka a řekl: "Kuř!" Pokladní začala usilovně a dobře kouřit... V tom lupič strhl masku a říká: "Aháá! Tak přece to jde! A doma my nemůžeme, doma je nám to protivný...!"',
         '"Miláčku, kolik jsi měla sexuálních partnerů?" "Proč mlčíš, ty mi to nechceš říct, viď?" "Já počítám."',
         'Mladá žena přistihne svého manžela in flagranti s milenkou. Oslepená žárlivostí se rozkřičí: Správně mi moje máma říkala, že jsi z těch chlapů, kteří každou ženskou hned zatáhnou do postele...! A ty, mami, ty na mě nečum! Taky jsi mě nasrala!',
         'Povídají si dvě kamarádky: "No představ si, co ten můj včera udělal. Normálně jdu do mrazáku, hledám kuře a ten můj přijde, vyhrne mi sukni a strčí mi ho tam." "Buď ráda, že je takovej aktivní." "No jo, jenže my jsme byli v Lidlu."',
         'Chlap volá domů ženě - honem přijeď za mnou do práce, mám na to hroznou chuť, rozdáme si to na pracovním stole. Žena: Vždyť tam máš sekretářku... Manžel: Fakt? Můžu? Tak díky a ahoj....',
         'Pohledný mladík jede nočním vlakem. V kupé sedí kromě něho jen jedna mladá dívka. Nádherný kousek. On čte, nevšímá si jí. Ona už to nevydrží: "Poslouchejte, jsme tu sami vy byste mě nechtěl?" On odloží časopis: "Slečno, raději jsem hodinu počkal, než abych vás tři hodiny přemlouval."',
         'Leží nahá žena v posteli. Přijde domů manžel a ptá se: "Proč tady ležíš nahá?" Manželka odpoví: "Nemám co na sebe!" Muž otevře skříň a počítá: "Jedny šaty-druhé-třetí-ahoj Karle-čtvrté..."',
         'On: "Máš pěkné tričko." \n Ona: "Děkuju .. a pod ním nic nemám." \n On: "Neboj se.. to doroste.."',
         'Kluk: "Něco bych lízal.. Ale ne, že to špatně pochopíš!" \n Holka: "Hmmm, aha. Tak pojďme na zmrzlinu." \n Kluk: "Věděl jsem, že to špatně pochopíš."',
         'Na pláži se ptá malá Anička maminky: "Co to tu má ten chlapeček?"Mamička se zarazila, avšak neztratila duchapřítomnost a pověděla první hloupost, která jí napadla."Víš, to je taká píšťalička."Za chvíli malá Anička přiběhne z pláčem a povídá mamince: "Mamí ona mu ale nepíská!"',
         'Lze oplodnit ženu za běhu? \n Nikoliv. \n Je vědecky dokázáno, že žena s vyhrnutou sukní běží až 4x rychleji než muž se staženýma kalhotama!',
         'Kluk: "Já bych chtěl udělat něco hloupého..." \n Holka: "Já jsem hloupá, udělej mě!"',
         'Vyleze chlap na pláži z vody, péro má až pod koleny. \n Všichni na něj koukají s vyvalenýma očima. \n "No co, ve vodě se každýmu trochu smrskne!"',
         'Prostitutka láká staršího zákazníka: "Tak co, ty navoněný fešáku, nedáme si spolu pár čísel?" \n "Jo... s tebou už jsem těch čísel zažil..." \n "My se známe?" ptá se prostitutka. \n "Aby ne... vždyť jsem tě na základce učil čtyři roky matematiku!"',
         'Hitler povídá Himlerovi: "Vyhladíme šest milionů židů a pět klaunů." \n Kolemjdoucí: "A proč 5 klaunů?" \n Hitler na to: "Vidíš já ti to říkal, že židi nebudou nikoho zajímat!"',
         'Život je jako šachy. Všichni nemůžou být bílí.',
         'Přijde černoch do obchodu a na rameni má velkého papouška. \n "Jé, ten je krásný," rozplývá se mladá prodavačka, "odkud ho máte?" \n "No přece z Afriky, tam jich je mnoho," odpoví papoušek.',
         'Znáte dvě nejtenčí knihy na světě? Jsou to somálská kuchařka a cikánský zákoník práce.',
         'Víte jaký je rozdíl mezi pneumatikou a černochem? \n Když dáte řetězy na pneumatiku, tak nezačne rapovat.',
         'Nejlepší fanoušci jsou židi: z vlaku rovnou do kotle.',
         'Podle mě se rasismus přehání, černoši se měli dřív jak v bavlnce.',
         'Můj humor je tak černej, že bych ho hned poslal sbírat bavlnu.',
         'Každý potřebuje trochu toho lidskýho tepla, ale jen Němci na to dokázali postavit továrny..',
         'Lord na svého afroamerického sluhu: \n "Johne, v Americe je prezident černoch, co na to říkáš?" \n "Jeho pán na něj musí být velice pyšný!"',
         'Příjde nácek do pekárny a říká: "Jeden chleba." \n Pekař na to: "Černý nebo bílý?" \n Nácek: "Provokuješ?!"',
         'Vykračuje si takhle chlapec se žlutou hvězdou na oděvu ghettem a voják na něj křičí "Hej, ty jsi Žid!" \n "Ne, ty vole, šerif."',
         'Jaký je rozdíl mezi negrem a srdcem? Srdci neporučís.',
         'Jdu takhle Londýnem a najednou proti mě negr a nese notebook. Říkám si: Ten vypadá jako můj. Ale to je blbost, můj je doma a leští mi boty.',
         'Co je to hnědá sračka mezi prstama u slonů? \n Pomalí černoši.',
         'SS: Žide, co děláš na tom stromě? \n Žid: Chytám bronz \n SS: Tak polez dolů, budeš chytat olovo.',
         'Kolik židů se vejde do kyblíku? \n Cca pět lopat.',
         'Bůh se snaží někomu dát přikázání, ale všude ho vyhazují. V Americe, v Evropě... \n Jde takhle po poušti a vtom potká Mojžíše a říká: "Hej, Žide, nechceš přikázání?" \n "A za kolik?" \n "Zadarmo." \n "Tak to jich beru deset!"',
         'Víte, jak poznáte autobus pro Židy? \n Jednoduše. Má výfuk vyvedenej dovnitř.',
         'Automobilka Škoda uvádí na trh nový typ Octavie pro čtyři osoby, nebo šestnáct cikánů.',
         'Otec se podívá na svého malého plešatého synka. \n "Stal se z tebe nácek, ty malej zmrde?" \n "Né tatínku, já mám leukémii!" \n " Leu co? Ještě budeš mluvit německy ty fašistická zrůdo?!"',
         'Snídá Hitler nad mapou housku a najednou kouká, že si podrobil Československo.',
         'Proč mají židi velký nosy? \n Vzduch je zdarma.',
         'Jaký je rozdíl mezi rohlíkem a židem? \n Rohlík v peci neřve.',
         'Víte proč Hitler spáchal na konci války sebevraždu?Přišel mu účet za plyn.',
         'Přivezou malého židovského kluka do koncentráku. Jeden ze Skopčáků se chvíli dívá na jeho žlutou hvězdu a povídá: "Hvězda, ty jsi Židáček." Klučina na to: "Ne, ty debile, já jsem tady nový šerif!"',
         'Nesnáším, když svého tmavého kamaráda ztratím ve tmě..',
         'Židovský pedofil potká v parku malou holčičku a povídá jí: "Holčičko, nechceš si koupit bonbón?"',
         'Vědci zjistili. že člověk se nedělí na rasy, ale má pouze jednu jedinou - člověka.Černí, žlutí a hnědí se nyní nebudou řadit mezi tento druh.',
         'Proč si Židé nehoní péro? Protože to všechno jde z vlastního pytlíku.',
         'Jak se říká černochovi, který řídí letadlo?Pilot, vy rasisti!',
         'Oznamuje tatínek rodině: \n "Rodino, těšte se, letos o dovolené poletíme k moři... \n Proč brečíš, Pepíčku?" \n "Já s vámi nemůžu, já ještě neumím létat."',
         'Pepíček dostane od tety krásné autíčko a maminka mu připomíná: "Co se říká?" \n "Nevím!" \n "Co říkám tatínkovi, když přinese výplatu?" \n "Aha - neříkej, že to je všechno!"',
         'Pepíček nechce jíst. Matka ho přemlouvá: \n "Miláčku, budeme si hrát na tramvaj. Ty budeš tramvaj a lžička s polévkou nastupující lidé." \n Pepíček polyká lžičku za lžičkou. Když už je talíř skoro prázdný, volá: \n "Konečná, všichni vystupovat!"',
         'Pepíček vběhne do třídy 5 minut po zvonění bez klepání. \n Paní učitelka mu povídá: "Pepíčku, pěkně se vrať a vejdi ještě jednou, ale tak, jak by vešel například tvůj tatínek. \n Pepíček vyjde, za chvíli rozkopne dveře, vrazí do třídy a zařve: "Tak co, vy kurvy! Nečekali jste mě, co?"',
         '„Pepíčku, skloňuj slovo chléb." \n „Kdo, co? - Chléb." \n „S kým, s čím? - Se salámem." \n „Komu, čemu? - Mně."',
         'Maminka jde s Pepíčkem poprvé do zoo. \n Od první chvíle, kdy tam vejdou, Pepíček nadšeně výská: "Jéé, opička, mamí, koukej, opička!" \n "Ticho, Pepíčku, to je teprve paní pokladní!"',
         'Pepíček prosí tátu: "Tati, kup mi buben." \n "Nekoupím, budeš mě rušit při práci." \n Pepíček: "Neboj, budu bubnovat jenom, když budeš spát."',
         'Paní učitelka se ptá: "Kde leží největší jezero?" \n Pepíček se hlásí, ale paní učitelka ho nechce vyvolat. \n Asi tak po půl hodině ho vyvolá a Pepíček povídá: "Největší jezero teď leží pode mnou."',
         'Pepíček přijde domů celý nadšený a chlubí se mamince: "Maminko, dnes jsme se ve škole učili o výbušninách!" \n Maminka se ptá: "A co se budete ve škole učit zítra?" \n Pepíček: "V jaké škole?"',
         'Přijde malý Pepíček domů z fotbalu a povídá: \n "Tatíí dal jsem dva góly!" \n "A jak to dopadlo?" \n "1:1"',
         'Malý Pepíček, který ještě neumí ani pořádně říct R, už jede sám tramvají a co víc, má v tašce vydru! \n Přistoupí dva policajti, chvíli čichají, ale pach rybiny je příliš silný, než aby se mýlili a tak se zeptají přímo Pepíčka: "Co to tady smrdí?" \n "Vydva"',
         'Přijde Pepíček do řeznictví a ptá se prodavačky: \n "Máte mozeček?" \n "Ne." \n "Tak proto vypadáte tak blbě!"',
         'Anička volá Pepíčkovi: "Pepíčku,přijď dneska večer k nám,nikdo nebude doma." \n Pepíček se navoní, učeše, obleče, přijde, zazvoní... \n A nikdo není doma.',
         'Ptá se učitelka Pepíčka: "Který pták je nejchytřejší?" \n "Vlaštovka" \n "Proč zrovna vlaštovka?" \n "Protože v září, na začátku školního roku, odlétá."',
         '"Mami, mami, mám dobrou a špatnou zprávu, jakou chceš slyšet první?" ptá se Pepíček maminky. \n "Tak tu dobrou." \n "Dostal jsem jedničku z diktátu!" \n "To je hezké, Pepíčku a jaká je ta špatná?" \n "Že to není pravda!"',
         '"V téhle třídě je třicet hlupáků!" nadává učitel. \n "Tčicetjedna!" povídá Pepíček. \n "Ty drzej fakane, okamžitě běž na chodbu!" \n "Abyste měl pravdu, co?"',
         'Pepíček dostane za trest napsat 100x "Nebudu tykat paní učitelce." \n Pepíček to napsal 200x, tak se ho učitelka zeptala, proč to napsal tolikrát. \n Pepíček odpoví: "Jsem ti chtěl udělat radost..."',
         'Pepíček: "Můj táta je fakt strašpytel!" \n Honzík: "Proč to?" \n Pepíček: "Pokaždé, když není mamka doma, spí u sousedky."',
         'Nechci vás strašit pane učiteli, říká Pepíček pedagogovi, ale tatínek říkal, že jestli nezačnu nosit lepší známky, dostane někdo pěknej výprask.',
         'Přijde Pepíček ze školy a říká mamince: \n "Dnes jsem se jako jediný ze třídy přihlásil!" \n "No to je pěkné, a na co se paní učitelka ptala?" \n "Kdo rozbil okno ne chodbě!"',
         'Učitelka vyvolá Pepíčka, aby vyjmenoval čtyři živly. \n "Zima, voda, oheň a ... hospoda!" zní odpověď. \n "Proč hospoda?" ptá se udiveně učitel. \n "Protože, když otec sedí v hospodě, tak maminka mu potom vždy říká, to si byl zase ve svém živlu!" odpoví Pepíček.',
         'Učitel ve škole se ptá dětí, jaké znají dráždidlo. \n Přihlásí se Mařenka a říká: "Kouř z cigaret." \n "Správně Mařenko." \n Pak se přihlásí Frantík a praví: "Pyl." \n "Správně, Frantíku." \n Najednou se přihlásí Pepíček a říká: "Pipinka." \n Rozzlobený učitel napíše Pepíčkovi poznámku. \n Druhý den hledá pan učitel Pepíčka, který si sedl do poslední lavice a ptá se: "Tak co ti na to řekl tatínek?" \n A Pepíček říká: "Tatínek pravil, že když pro vás není pipinka dost dobré dráždidlo, tak jste buzerant a mám si sednout do poslední lavice..."',
         'Přijde Pepíček ze školy a říká mamince: \n "Dnes jsem se jako jediný ze třídy přihlásil!" \n "No to je pěkné, a na co se paní učitelka ptala?" \n "Kdo rozbil okno ne chodbě!"',
         'Okolo pískoviště jede paní a vidí Pepíčka a povídá: "Taky bych chtěla takového krásného chlapečka. Já to furt zkouším s čápem a pořád nic." \n Pepíček: "Madam, tak to zkuste s jiným ptákem."',
         'Pepíček se ptá: "Tatínku, kde má srdíčko nožičky?" \n "Žádné nemá, samozřejmě." odpoví tatínek, "Jak jsi na to přišel?" \n "Já jsem včera slyšel, jak říkáš: Srdíčko, roztáhni nožičky!"',
         'Ve škole se dětí učí hospodárně zacházet s penězi, \n a každý dostane na útratu 10 kč a má podat vysvětlení, jak s ní naložil. Mařenka říká " já koupila za 10 kč broskvičku, snědla, pecku zasadilaa vyroste mě stomeček plný broskviček" " Výborně", raduje se paní učitelka. Honzík říká " Já koupil meruňku, snědl a také zasadil" " Výborně, výborně" Opět se paní učitelka raduje. V tom se přihlásí Pepíček a říká" Já jsem si koupil jitrnici, nejdříve se s ní sestra pohlavně ukojila, potom jsme ji snědli k večeři, v noci tatínek použil střívko jako prezervativ, ráno jsme do ní nasrali a maminka jí došla vrátit do obchodu, že je zkažená a tady Vám vracím tu desetikorunu"...',
         'Anička a Pepíček sedí na louce plné květů a dívají se, jak si to rozdává býk jalovičkou. \n Anička se optá Pepíčka: "Pepíčku, jak to ten býk ví, že to ta jalovička chce?" \n Pepíček: "On to vycítí." \n Anička: "A ty máš kurva rýmu nebo co?!"',
         'Pepíček nakreslí sprostý obrázek na tabuli. \n Druhý den si paní učitelka pozve tatínka do svého kabinetu a začne, ten váš Pepíček... ani si nedovedete představit co ten váš chlapec včera nakreslil. \n Tatínek odvětí, ale dovedu, minulý týden nakreslil doma na sporák píču... já si spálil držku a dědek kokota.',
         'Pepíček vejde do ložnice a vidí jak si to rodiče rozdávaj v posteli. Otec se zasměje a hodí po něm polštář.Za chvíli otec zaslechne divné zvuky z Pepíčkova pokoje, nakoukne a vidí, jak si to tam Pepíček rozdává s babičkou. Ten koukne na zkoprnělýho otce ve dveřích a povídá: "Není to zas taková prdel, když ti někdo píchá matku, viď?"',
]

def handle_response(message: str, username) -> str:
    p_message = message.lower()
    if p_message in ["čau", "cau", "ahoj"]:
        return f'Ahoj `{username[:-5]}`'

    if p_message == 'kostky':
        rand = str(random.randint(1, 6))
        if rand == "1":
            return "_1️⃣_"
        if rand == "2":
            return "_2️⃣_"
        if rand == "3":
            return "_3️⃣_"
        if rand == "4":
            return "_4️⃣_"
        if rand == "5":
            return "_5️⃣_"
        if rand == "6":
            return "_6️⃣_"

    if p_message == '!pomoc':
        return "`Nasrat, pomož si sám`"

    if p_message == 'vtip':
        return str(random.choice(vtipy))

    #  return 'Yeah, I don\'t know. Try typing "!help".'