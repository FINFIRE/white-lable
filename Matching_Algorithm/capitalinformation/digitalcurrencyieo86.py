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

def digitalcurrencyieo(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Digital Currency</b></u><br>
    Capital Type: Initial Exchange Offering </center></p>
    <p><b><u>Introduction</u></b><br>
An Initial Exchange Offering (IEO) is a digital asset fundraising mechanism in which a cryptocurrency exchange facilitates the sale of a startup's tokens directly to investors on its platform. Unlike an Initial Coin Offering (ICO), where the issuing company manages the token sale independently, an IEO is conducted through a centralized exchange that performs due diligence, marketing, and investor onboarding. {n} fits that definition. IEOs gained prominence in 2019 after several high-profile exchange-led offerings successfully raised millions within minutes. For example, Binance launched its Binance Launchpad platform, where early IEOs reportedly raised over $7 million in under 20 minutes. IEOs offer enhanced investor confidence compared to ICOs due to exchange vetting, though regulatory and market risks remain.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.An Initial Exchange Offering (IEO) is a token fundraising event administered by a cryptocurrency exchange on behalf of a blockchain startup. The exchange hosts the token sale, manages investor verification, and distributes tokens to participants. Investors must hold an account with the hosting exchange and often use the exchange's native cryptocurrency to participate. By leveraging the exchange's infrastructure and user base, startups gain immediate market exposure and credibility. (SEC, 2019)
<br>


    <br>2.  IEOs are best suited for blockchain startups, decentralized application developers, and Web3 platforms seeking rapid fundraising combined with exchange-backed credibility. Projects with working prototypes, strong tokenomics, and scalable blockchain applications are more likely to be accepted by reputable exchanges. Exchanges conduct internal due diligence before listing an IEO, making this model more selective than traditional ICOs. (Investopedia, n.d.)
<br>

    <br>3. IEOs emerged in 2019 as a response to declining investor trust in ICOs following regulatory scrutiny and fraud cases in 2017-2018. By shifting fundraising to centralized exchanges, projects benefited from exchange-level due diligence and built-in investor communities. Major exchanges such as Binance and Huobi pioneered launchpad platforms that standardized token sales. Although IEOs restored some investor confidence, regulatory frameworks across jurisdictions remain under development. (World Economic Forum, 2019)
<br>
    <br>4.Despite exchange oversight, IEOs carry substantial risks. Token price volatility, cybersecurity threats, regulatory uncertainty, and market speculation can significantly impact outcomes. Projects are dependent on the hosting exchange's reputation and operational stability. Regulatory agencies may classify certain tokens as securities, triggering compliance obligations under securities laws. (Harvard Law School Forum, 2018)
<br>
    <br>5. To conduct an IEO, a startup must apply to a cryptocurrency exchange's launchpad program and undergo due diligence, including technical review, business evaluation, and compliance checks. The project must provide a detailed whitepaper, token economics model, roadmap, and legal compliance documentation. Strong community engagement, transparent governance, audited smart contracts, and clear token utility significantly improve approval chances. (World Economic Forum, 2019)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (n.d.). Initial Exchange Offering (IEO). <a href="https://www.investopedia.com">https://www.investopedia.com</a>
<br>
    <br>U.S. Securities and Exchange Commission. (2019). Framework for "Investment Contract" Analysis of Digital Assets. <a href="https://www.sec.gov">https://www.sec.gov</a>
<br>
    <br>Harvard Law School Forum on Corporate Governance. (2018). Regulatory issues in token offerings. <a href="https://corpgov.law.harvard.edu">https://corpgov.law.harvard.edu</a>
<br>
    <br>World Economic Forum. (2019). Guidelines for Digital Token Offerings. <a href="https://www.weforum.org">https://www.weforum.org</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Legally Registered Business Entity
<br>•   Compliance with Securities and Financial Regulations (if applicable)
<br>•   AML/KYC Compliance for Investors (managed by exchange)
<br>•   Transparent Whitepaper and Risk Disclosure
<br>•   Smart Contract Audit
<br>•   Tax Compliance
<br>•   Data Protection & Cybersecurity Measures
<br>•   Exchange Due Diligence Approval


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   IEO Whitepaper
<br>•   Tokenomics & Distribution Model
<br>•   Smart Contract Code & Audit Report
<br>•   Corporate Registration Documents
<br>•   Risk Disclosure Statement
<br>•   AML/KYC Policy
<br>•   Business Plan & Roadmap
<br>•   Exchange Application & Due Diligence Package
<br>•   Legal Opinion (if required)

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencyieofaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Digital Currency<br>
    Initial Exchange Offering</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is an Initial Exchange Offering (IEO)?</u></b><br>
    •Answer: An Initial Exchange Offering (IEO) is a token fundraising event conducted through a cryptocurrency exchange, where the exchange facilitates the sale of tokens on behalf of a blockchain project.
</p>

    <p><u><b>2. How does an IEO differ from an ICO?</u></b><br>
    •Answer: In an IEO, the cryptocurrency exchange manages the token sale and investor onboarding, while in an ICO the project conducts the fundraising independently.
</p>

    <p><u><b>3. Who conducts the token sale in an IEO?</u></b><br>
    •Answer: The cryptocurrency exchange hosts and administers the offering, handling compliance checks, marketing, and token distribution.
</p>

    <p><u><b>4. What do investors receive in an IEO?</u></b><br>
    •Answer: Investors receive digital tokens that may represent utility, governance rights, or other blockchain-based functions.
</p>

    <p><u><b>5. Are IEO tokens considered securities?</u></b><br>
    •Answer: Classification depends on token structure and jurisdiction, and some IEO tokens may be regulated as securities.
</p>

    <p><u><b>6. What are the benefits of an IEO for projects?</u></b><br>
    •Answer: Benefits include enhanced credibility, access to the exchange's user base, simplified compliance processes, and faster market exposure.
</p>

    <p><u><b>7. What are the risks of investing in an IEO?</u></b><br>
    •Answer: Risks include token price volatility, project failure, regulatory changes, cybersecurity threats, and potential loss of capital.
</p>

    <p><u><b>8. How are investors vetted in an IEO?</u></b><br>
    •Answer: Exchanges typically require Know Your Customer (KYC) and Anti-Money Laundering (AML) verification before participation.
</p>

    <p><u><b>9. Can IEO tokens be traded immediately after the sale?</u></b><br>
    •Answer: In many cases, tokens are listed on the hosting exchange shortly after the offering, enabling secondary market trading.
</p>

    <p><u><b>10. How much capital can be raised through an IEO?</u></b><br>
    •Answer: Fundraising amounts vary significantly depending on project demand, exchange reputation, and market conditions.
</p>

    <p><u><b>11. What is the role of the exchange in due diligence?</u></b><br>
    •Answer: Exchanges often conduct project reviews and technical evaluations before approving an IEO, adding a layer of screening.
</p>

    <p><u><b>12. Are IEOs regulated?</u></b><br>
    •Answer: Regulatory treatment varies by country, and exchanges must comply with applicable securities and financial regulations.
</p>

    <p><u><b>13. What fees are associated with an IEO?</u></b><br>
    •Answer: Projects typically pay listing fees and may share a percentage of funds raised with the exchange.
</p>

    <p><u><b>14. How does an IEO benefit investors compared to an ICO?</u></b><br>
    •Answer: Investors may benefit from exchange vetting, integrated custody, and immediate liquidity through exchange listing.
</p>

    <p><u><b>15. When should a blockchain project consider launching an IEO?</u></b><br>
    •Answer: A project may consider an IEO when seeking exchange-backed fundraising, broader investor reach, and faster token market access.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencyieotwelve(request):
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
    Capital Type: Initial Exchange Offering</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
An Initial Exchange Offering (IEO) is best suited for early-stage to growth-stage blockchain projects that have a completed or near-complete MVP, a defined token model, and demonstrable traction or community interest. Compared to an ICO, IEO projects are typically more developed due to exchange vetting requirements.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
IEOs are commonly structured through C-Corporations, LLCs, or offshore crypto foundations. Projects must meet compliance standards of the hosting cryptocurrency exchange, often requiring formal corporate structure and governance documentation.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Before launching an IEO, projects generally need a published whitepaper, completed tokenomics, smart contract audits, legal opinion regarding token classification, and exchange due diligence approval. Exchange approval is mandatory prior to public sale.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
IEOs operate within the digital asset capital markets, facilitated by centralized cryptocurrency exchanges such as Binance, KuCoin, and OKX. Unlike ICOs, investor participation occurs directly on the exchange platform.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
IEO raises typically range from $500,000 to $20 million, depending on exchange size, market cycle conditions, and project demand. Top-tier exchanges may facilitate larger raises during strong market cycles.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
IEOs are token issuance events, not equity rounds. Investors receive exchange-listed tokens, which may trade immediately after the sale concludes.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
IEOs often include private seed/pre-sale rounds, exchange-hosted public sale, and immediate token distribution. Many exchanges use lottery or tiered allocation systems for participants.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds are typically allocated toward:
<br>•   Product development and platform scaling
<br>•   Marketing and ecosystem incentives
<br>•   Liquidity support
Use of funds is usually disclosed in the whitepaper and exchange offering materials.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk level is very high, including regulatory uncertainty, market volatility, exchange platform risk, token price instability, and smart contract vulnerabilities. While exchange vetting reduces fraud risk compared to ICOs, it does not eliminate investment risk.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Cost includes exchange listing fees (can be substantial), token allocation to exchange, marketing requirements, and legal and compliance expenses. There is no traditional equity dilution unless structured separately.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are high, including legal structuring, smart contract audits, exchange due diligence fees, and marketing campaigns. Exchange listing costs may range from significant fixed fees to revenue-sharing agreements.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing is typically 3-6 months, depending on exchange approval timeline, technical readiness, and market conditions. IEOs can deploy capital faster than traditional venture rounds once approved.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
