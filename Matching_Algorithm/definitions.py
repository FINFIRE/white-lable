from django.utils.safestring import mark_safe

definitions ={
    'Private Equity Securities - Simple Agreement Future Equity':mark_safe("""<p><u><b>Match - Private Equity Securities - Simple Agreement Future Equity</u></b><br>
            A Simple Agreement for Future Equity (SAFE) is a financing contract that may be used by a
            startup company to raise capital in its seed financing rounds. A SAFE is an investment 
            contract between a startup and an investor that gives the investor the right to receive 
            equity of the company on certain triggering events, such as a: 1) future equity financing (known 
            as a next equity financing or qualified financing), usually led by an institutional venture 
            capital (VC) fund; and 2) Sale of the company: the price of the equity that the SAFE holders 
            receive on conversion is lower than the price of the securities issued to VC investors in 
            connection with a next equity financing, based on either a discount rate or valuation cap. 
            A SAFE is viewed by some as a more founder-friendly alternative to convertible notes.
            </p>
            <p>
            •	all purchasers in the offering are accredited investors.
            <br>•	the issuer takes reasonable steps to verify their accredited investor status; and
            <br>•	certain other conditions in Regulation D are satisfied."
            </p>
            <p>
            SAFEs all have the same conversion features as convertible notes but lack the debt hallmarks.
            In particular, a SAFE has no: maturity date, until a conversion event occurs; SAFEs remain outstanding
            indefinitely. Accruing interest- investors receive only a right to convert their SAFEs into equity at a
            lower price than the investors in the subsequent financing (based either on the discount or valuation cap in their SAFEs).
            </p><p>
            SAFEs are a relatively recent addition (2013) to the seed financing, security crowdfunding toolkit, popularized by the premier 
            startup accelerator, Y Combinator. Other players in the startup finance ecosystem have created 
            form documents similar to the SAFE but using different names. These include: the convertible 
            security proposed by a partner at the law firm of Wilson Sonsini Goodrich & Rosati and the Keep 
            it Simple Security (KISS) created by 500 Startups, another startup accelerator.
            </p>"""),

    "Private Equity Securities - Regulation D 506(c)":mark_safe("""<p><u><b>Match Private Equity Rule 506(c) of Regulation D (Title II of the JOBS Act)</u></b><br>
            Section 201(a) of the JOBS Act requires the SEC to eliminate the prohibition on using general 
            solicitation under Rule 506 where all purchasers of the securities are accredited investors, and 
            the issuer takes reasonable steps to verify that the purchasers are accredited investors. To 
            implement Section 201(a), the SEC adopted paragraph (c) of Rule 506. Under Rule 506(c), issuers 
            can offer securities through means of general solicitation, provided that:</p>
            <p>
            <br>• all purchasers in the offering are accredited investors.
            <br>• the issuer takes reasonable steps to verify their accredited investor status; and
            <br>• certain other conditions in Regulation D are satisfied.
            </p>
            <p><u><b>Accredited Investors:</b></u><br>
            “Accredited investor” is a term used by the Securities and Exchange Commission (SEC) under
             Regulation D to refer to investors who are financially sophisticated and have a reduced 
             need for the protection provided by certain government filings. In order for an individual
            to qualify as an accredited investor, he or she must accomplish at least one of the 
            following: 1) earn an individual income of more than $200,000 per year, or a joint income 
            of $300,000, in each of the last two years and expect to maintain the same level of income;
             2) have a net worth exceeding $1,000,000, either individually or jointly with a spouse; 
             and 3) be a general partner, executive officer, director or a related combination thereof 
             for the issuer of a security being offered."
            </p> """),

   "Private Equity Securities - Regulation A":mark_safe("""<p><u><b>Private Equity Securities - Regulation A</u></b><br>
                <p>In the first half of 2024, over $91 million was raised using Regulation A investments. In 2023,
                Reg A offerings that were publicly available on major platforms and through the issuer’s own
                websites raised $225 million. The total valuation of all equity Regulation A (Reg A) companies
                raising in May 2023 was $6.6 billion. On average, each Reg A raise in May 2023 had a valuation
                of $152.7 million.</p>                
                """),

   "Small Business Administration 504B":mark_safe("""<p><u><b>Small Business Administration 504</u></b><br>
                In FY23, the SBA’s 504 program delivered more than 5,900 fixed-rate loans for equipment, real
                estate, and debt refinancing worth more than $6.4 billion to small businesses. In the first half of
                2024 the SBA approved 3,306 504 loans for $3,619,017,000.</p>
                """),

   "Private Equity Securities - Convertible Note":mark_safe("""<p><u><b>Private Equity Securities - Convertible Note</u></b><br>
                Issuance of convertible securities for the first half of 2024 has been particularly strong with
                approximately $40 billion of new issuance coming to the market. Our expectation is that
                issuance will meet or exceed $80 billion this year which compares to $53.4 billion of new
                issuance in 2023 and $28.7 billion of new issuance in 2023. According to the Angel Capital
                Association’s 2020 Angel Funders Report, 37% of angel deals were done using convertible
                notes. From a representative sample of worldwide startups, it seems that convertible notes are
                used 33,02% of the times for seed funding and 62,53% for bridge financing.</p>
                """),
   
   "Commercial Banking - Commercial Banking Loan":mark_safe("""<p><u><b>Commercial Banking - Commercial Banking Loan</u></b><br>
                Commercial and industrial loans granted by U.S. commercial banks amounted to approximately
                2.8 trillion U.S. dollars from January to April in 2024.</p>"""),
                
    "Private Equity Securities - Regulation CF Tittle III":mark_safe("""<p><u><b>Private Equity Securities - Regulation CF Tittle III</u></b><br>
                There are 86 FINRA regulated Reg CF platforms. More than 6,500 U.S. startups and other small
                businesses have raised nearly $2.48B in capital through 8,400 investment rounds. In most cases,
                these companies were too early stage for venture capital or private equity. With competition for
                angel investors being intense, equity crowdfunding provides an ability to raise capital from the
                crowd, and not to be forced to rely on bank loans or credit card debt to fund a small business.
                More than 2,000,000 Americans have invested in Reg CF offerings, averaging about $1,200 per
                investment.</p>"""),
    "Private Equity Securities - Regulation D 506(b)":mark_safe("""<p><u><b>Private Equity Securities - Regulation D 506(b)</u></b><br>
                According to the SBAO Report, Rule 506(b) remains the overwhelming choice for capital raises
                among small businesses, with a total offering of $2.7 Trillion and a median raise of $1.2 Million.
                Once again, the aggregate amount raised under Rule 506(b) far outstripped the amount raised via
                initial public offerings (IPO), which raised only $17 Billion. Regulation A offerings, often called
                “mini-IPOs,” raised $1.5 Billion.</p>"""),

    "Commercial Banking - Line of Credit": mark_safe("""<p><u><b>Commercial Banking - Line of Credit</u></b><br>
                Most lenders — both online and traditional — advertise lending amounts within $5,000 to
                $500,000. However, if you need more cash, you may be able to find it. Wells Fargo offers a
                secured business line of credit that can go up to $1 million. Bank of America lines of credit begin
                at $1,000 but have no set-in-stone ceiling.<br>
                Meanwhile, the online loan marketplace Lendio has a limit of $500,000 and accepts applications
                from companies with a credit score as low as 600. Some online lenders also offer funds for
                companies as young as six months in operation. One such lender, Credibly, caps lines at
                $300,000.</p>"""),

    "Small Business Administration (SBA) - SBA Veteran":mark_safe("""<p><u><b>Small Business Administration (SBA) - SBA Veteran</u></b><br>
                Fiscal year 2024 marked a notable rise in SBA-backed loans, with more than 3,100 loans issued
                to veteran-owned small businesses, totaling $1.3 billion. Total loans are up almost 48% under the
                Biden-Harris Administration, and total loan dollars are up 51%. This progress illustrates the
                SBA’s dedication to helping veteran entrepreneurs access essential funding, ensuring they have
                the resources needed to launch and grow their businesses.</p>""")                                                                       
}