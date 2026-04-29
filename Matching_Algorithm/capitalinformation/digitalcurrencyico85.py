from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases

def digitalcurrencyico(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Digital Currency</b></u><br>
    Capital Type: Initial Coin Offering </center></p>
    <p><b><u>Introduction</u></b><br>
An Initial Coin Offering (ICO) is a blockchain-based fundraising method in which a company issues digital tokens or coins to investors in exchange for cryptocurrency (such as Bitcoin or Ethereum) or fiat currency to finance a project or platform. {n} fits that definition. ICOs gained significant popularity during the cryptocurrency boom between 2017 and 2018, when startups collectively raised over $20 billion globally through token offerings. Unlike traditional equity financing, ICO investors typically receive utility tokens or digital assets rather than ownership shares. ICOs allow startups to access global capital markets rapidly, but they also involve regulatory uncertainty, high volatility, and investor risk.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.An Initial Coin Offering (ICO) is a decentralized fundraising mechanism in which blockchain-based startups issue digital tokens to investors in exchange for capital. These tokens may grant access to a platform (utility tokens) or represent investment-like interests (security tokens). ICOs operate using distributed ledger technology, typically on platforms such as Ethereum, and are marketed globally via online channels. Regulatory authorities such as the U.S. Securities and Exchange Commission have clarified that certain tokens may qualify as securities depending on their characteristics. (SEC, 2017)
<br>


    <br>2.  ICOs are best suited for blockchain-based startups, decentralized application (dApp) developers, fintech platforms, and Web3 infrastructure projects seeking global participation. Companies with strong technical foundations, clear token utility models, and active developer communities benefit most. Projects in decentralized finance (DeFi), gaming, data storage, and digital identity sectors frequently utilize ICOs to bootstrap ecosystems and incentivize early adopters. (Investopedia, n.d.)
<br>

    <br>3. ICOs emerged around 2013 as an alternative to venture capital funding, gaining prominence in 2017 during the cryptocurrency market expansion. The rapid growth of token sales attracted global participation but also led to fraudulent schemes and regulatory scrutiny. Following enforcement actions by regulators, including guidance issued by the SEC in its 2017 DAO Report, the ICO market declined and evolved into more regulated alternatives such as Security Token Offerings (STOs) and Initial Exchange Offerings (IEOs). (SEC, 2017; World Economic Forum, 2019)
<br>
    <br>4.ICOs carry substantial risks for both issuers and investors. Regulatory uncertainty remains a major concern, as many jurisdictions classify certain tokens as securities, subjecting issuers to compliance obligations. Market volatility in cryptocurrencies can significantly affect fundraising value. Additionally, lack of investor protections, cybersecurity risks, fraud, and project failure rates contribute to high risk. (Harvard Law School Forum, 2018)
<br>
    <br>5.
To conduct a successful ICO, a company must develop a blockchain-based project, create a token smart contract, and publish a comprehensive whitepaper outlining the business model, token economics, roadmap, and risks. Compliance with local securities and AML/KYC regulations is critical. Successful ICOs typically demonstrate strong technical capability, transparent governance, active community engagement, and clear utility for the issued token. (World Economic Forum, 2019)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (n.d.). Initial Coin Offering (ICO). <a href="https://www.investopedia.com">https://www.investopedia.com</a>
<br>
    <br>U.S. Securities and Exchange Commission. (2017). Report of Investigation Pursuant to Section 21(a): The DAO. <a href="https://www.sec.gov">https://www.sec.gov</a>
<br>
    <br>Harvard Law School Forum on Corporate Governance. (2018). Regulatory challenges of ICOs. <a href="https://corpgov.law.harvard.edu">https://corpgov.law.harvard.edu</a>
<br>
    <br>World Economic Forum. (2019). Guidelines for digital token offerings. <a href="https://www.weforum.org">https://www.weforum.org</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Legally Registered Entity (depending on jurisdiction)
<br>•   Compliance with Securities Laws (if token qualifies as a security)
<br>•   AML/KYC Procedures for Investors
<br>•   Transparent Whitepaper and Risk Disclosure
<br>•   Smart Contract Audit (recommended for security)
<br>•   Tax Compliance
<br>•   Data Protection and Cybersecurity Measures
<br>•   Regulatory Filing (if required in jurisdiction)


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   ICO Whitepaper
<br>•   Token Economics Model
<br>•   Smart Contract Code & Audit Report
<br>•   Corporate Registration Documents
<br>•   Risk Disclosure Statement
<br>•   AML/KYC Compliance Policy
<br>•   Marketing & Token Distribution Plan
<br>•   Financial Projections / Roadmap
<br>•   Legal Opinion (if applicable)

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencyicofaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Digital Currency<br>
    Initial Coin Offering</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is an Initial Coin Offering (ICO)?</u></b><br>
    •Answer: An Initial Coin Offering (ICO) is a fundraising method in which a company or project issues digital tokens to investors in exchange for cryptocurrency or fiat money.
</p>

    <p><u><b>2. How does an ICO work?</u></b><br>
    •Answer: A project creates and sells blockchain-based tokens to investors, typically before the product is fully developed, to raise capital for development and operations.
</p>

    <p><u><b>3. What do investors receive in an ICO?</u></b><br>
    •Answer: Investors receive digital tokens, which may represent utility access, governance rights, or, in some cases, investment interests depending on the structure.
</p>

    <p><u><b>4. Are ICO tokens considered securities?</u></b><br>
    •Answer: ICO tokens may be classified as securities depending on their structure and jurisdiction, particularly if they promise profit based on the efforts of others.
</p>

    <p><u><b>5. Who can participate in an ICO?</u></b><br>
    •Answer: Participation rules vary by jurisdiction; some ICOs are open globally, while others restrict participation to accredited or qualified investors.
</p>

    <p><u><b>6. What is a whitepaper in an ICO?</u></b><br>
    •Answer: A whitepaper is a document outlining the project's vision, technology, token economics, roadmap, and risks.
</p>

    <p><u><b>7. How much capital can be raised through an ICO?</u></b><br>
    •Answer: ICO fundraising amounts vary widely, ranging from hundreds of thousands to hundreds of millions of dollars depending on market demand.
</p>

    <p><u><b>8. What are the benefits of an ICO for companies?</u></b><br>
    •Answer: Benefits include global investor access, fast capital raising, minimal traditional intermediaries, and community building.
</p>

    <p><u><b>9. What are the risks of investing in an ICO?</u></b><br>
    •Answer: Risks include high volatility, regulatory uncertainty, project failure, fraud, cybersecurity threats, and potential total loss of investment.
</p>

    <p><u><b>10. Are ICOs regulated?</u></b><br>
    •Answer: Regulation varies by country, and many jurisdictions have introduced securities laws or restrictions governing token offerings.
</p>

    <p><u><b>11. How are ICO tokens distributed?</u></b><br>
    •Answer: Tokens are typically distributed to investors through blockchain transactions after payment is received.
</p>

    <p><u><b>12. What is the difference between an ICO and an IPO?</u></b><br>
    •Answer: An ICO issues digital tokens on a blockchain, while an IPO issues company shares through regulated public markets.
</p>

    <p><u><b>13. Can ICO tokens be traded after issuance?</u></b><br>
    •Answer: Yes, many tokens can be traded on cryptocurrency exchanges, subject to exchange listings and regulatory compliance.
</p>

    <p><u><b>14. What is tokenomics in an ICO?</u></b><br>
    •Answer: Tokenomics refers to the economic structure of the token, including supply, distribution, incentives, and utility within the ecosystem.
</p>

    <p><u><b>15. When should a company consider launching an ICO?</u></b><br>
    •Answer: A company may consider an ICO when building a blockchain-based project that benefits from token utility, community participation, and decentralized funding mechanisms.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencyicotwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Digital Currency</b></u><br>
    Capital Type: Initial Coin Offering</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Initial Coin Offerings (ICOs) are best suited for early-stage blockchain or decentralized technology projects, typically at the concept, whitepaper, or early product development stage. Some later-stage crypto projects also use ICO-style raises for ecosystem expansion.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
ICOs are typically structured through C-Corporations, LLCs, or offshore entities established in crypto-friendly jurisdictions. Many projects create a foundation or special purpose entity (SPE) to issue tokens and manage protocol governance.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Projects usually require a published whitepaper, defined tokenomics (supply, allocation, utility), a technical roadmap, and legal review regarding securities classification. Prior funding is not required but may improve credibility.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
ICOs operate within the global digital asset market, often outside traditional banking systems. Regulatory classification may vary depending on whether the token is considered a utility token or security token, which significantly impacts compliance obligations.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
ICO raises historically ranged from hundreds of thousands to hundreds of millions of dollars, depending on market conditions, investor demand, and project credibility.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
ICOs function as a token issuance event, not a traditional equity round. Investors typically receive digital tokens rather than company ownership, unless structured as a security token offering.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Token sales may occur in private pre-sale rounds, public token sale phases, and multiple pricing tiers. Funds are usually received immediately upon token purchase.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Use of funds is generally disclosed in the whitepaper and may include:
<br>•   Protocol development
<br>•   Marketing and ecosystem growth
<br>•   Liquidity provisioning
<br>•   Operational expenses
Misuse of funds can lead to reputational and regulatory consequences.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is extremely high, including regulatory enforcement risk, market volatility, cybersecurity breaches, smart contract vulnerabilities, and investor litigation risk. Investor protections are often limited.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
There is no traditional equity dilution unless equity is separately issued. However, token issuance creates economic dilution within the token supply, and founders often allocate significant token percentages to investors.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate to high, including legal and regulatory consultation, smart contract development and audits, marketing and community building, and exchange listing fees.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital can be fast, often 2-4 months from whitepaper publication to token sale, depending on development readiness and regulatory positioning.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
