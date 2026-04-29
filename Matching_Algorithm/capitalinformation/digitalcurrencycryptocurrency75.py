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

def digitalcurrencycryptocurrency(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Digital Currency</b></u><br>
    Capital Type: Cryptocurrency </center></p>
    <p><b><u>Introduction</u></b><br>
Cryptocurrency is ideal for users and investors seeking decentralized digital assets that enable peer-to-peer value transfer without reliance on traditional financial intermediaries. It is designed so that value is represented by cryptographically secured tokens operating on distributed ledger technology (blockchain), with transaction validation achieved through consensus mechanisms rather than centralized authorities. {n} fits that definition. In 2026, cryptocurrencies remain a foundational component of the digital asset ecosystem, encompassing payment-focused coins, smart-contract platforms, and utility-driven networks. Major cryptocurrencies are used for payments, remittances, decentralized finance (DeFi), non-fungible tokens (NFTs), and on-chain governance, with global participation across retail, institutional, and sovereign actors. While cryptocurrencies offer transparency, programmability, and censorship resistance, they introduce price volatility, regulatory uncertainty, and technological risk. Market sentiment, protocol security, and evolving legal frameworks can materially affect valuation, usability, and adoption.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Cryptocurrency is a digital asset that uses cryptographic techniques and distributed ledger technology to secure transactions, control the creation of new units, and verify asset transfers without reliance on a central issuing authority. (Investopedia, 2025)
<br>


    <br>2.  Cryptocurrencies exist outside the traditional Capital Stack, as they do not represent equity ownership or debt obligations. Instead, they function as native digital assets used for exchange, settlement, network participation, or value storage within blockchain ecosystems. (Bank for International Settlements, 2025)
<br>

    <br>3. Structurally, cryptocurrencies operate on blockchain networks governed by protocol rules, consensus mechanisms (such as proof-of-work or proof-of-stake), and open-source software maintained by decentralized developer communities. Network upgrades are implemented through protocol changes rather than corporate actions. (Ethereum Foundation, 2025)
<br>
    <br>4.From a risk perspective, cryptocurrencies are exposed to market volatility, protocol vulnerabilities, governance disputes, and regulatory intervention. Security breaches, forks, or adverse legal developments can materially impair asset value and network functionality. (International Monetary Fund, 2025)
<br>
    <br>5.
From an accounting and process standpoint, cryptocurrencies are typically classified as Intangible Assets or Digital Assets, depending on jurisdiction and use case. Transactions are settled on-chain, with custody, valuation, and reporting dependent on market liquidity and technological controls. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). Cryptocurrency Definition and Uses. <a href="https://www.investopedia.com/cryptocurrency">https://www.investopedia.com/cryptocurrency</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Cryptoassets and Financial Stability. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Ethereum Foundation. (2025). Blockchain and Consensus Mechanisms. <a href="https://ethereum.org">https://ethereum.org</a>
<br>
    <br>International Monetary Fund (IMF). (2025). Digital Assets and the Global Financial System. <a href="https://www.imf.org">https://www.imf.org</a>
<br>
    <br>Deloitte. (2025). Accounting and Tax Considerations for Cryptocurrencies. <a href="https://www2.deloitte.com/digital-assets">https://www2.deloitte.com/digital-assets</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Network Participation - Access to blockchain protocol
<br>•   Wallet Infrastructure - Secure private key custody
<br>•   Exchange Compliance - KYC/AML requirements for fiat on-ramps
<br>•   Regulatory Awareness - Jurisdictional crypto asset rules
<br>•   Tax Reporting - Capital gains and transaction reporting
<br>•   Smart Contract Interaction - Technical competence and security
<br>•   Sanctions Compliance - Address screening where applicable
<br>•   Disclosure & Risk Acknowledgement - User and investor awareness


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Blockchain Whitepaper - Protocol design and purpose
<br>•   Token Specification - Supply, issuance, and mechanics
<br>•   Network Governance Documentation - Upgrade and voting processes
<br>•   Audit Reports - Protocol and smart-contract security
<br>•   Wallet & Custody Policies - Asset protection procedures
<br>•   Exchange Listings - Market access documentation
<br>•   Regulatory Guidance - Applicable jurisdictional rules
<br>•   Transaction Records - On-chain activity history

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencycryptocurrencyfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Digital Currency<br>
    Cryptocurrency</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is cryptocurrency?</u></b><br>
    •Answer: Cryptocurrency is a digital or virtual currency that uses cryptography and blockchain technology to enable secure, decentralized transactions.
</p>

    <p><u><b>2. How does cryptocurrency work?</u></b><br>
    •Answer: Cryptocurrencies operate on decentralized blockchain networks where transactions are recorded on a distributed ledger.
</p>

    <p><u><b>3. Who issues cryptocurrencies?</u></b><br>
    •Answer: Most cryptocurrencies are not issued by a central authority; they are created and maintained through decentralized protocols.
</p>

    <p><u><b>4. What are common examples of cryptocurrencies?</u></b><br>
    •Answer: Examples include Bitcoin, Ethereum, and other blockchain-based digital currencies.
</p>

    <p><u><b>5. What are cryptocurrencies used for?</u></b><br>
    •Answer: They are used for payments, investments, value transfer, decentralized applications, and financial innovation.
</p>

    <p><u><b>6. Are cryptocurrencies legal?</u></b><br>
    •Answer: Legality varies by country and is subject to evolving regulatory frameworks.
</p>

    <p><u><b>7. Can cryptocurrencies be traded?</u></b><br>
    •Answer: Yes, cryptocurrencies can be traded on digital exchanges and peer-to-peer platforms.
</p>

    <p><u><b>8. Are cryptocurrencies considered high risk?</u></b><br>
    •Answer: Yes, they are highly volatile and carry market, regulatory, and technology risks.
</p>

    <p><u><b>9. How are cryptocurrencies secured?</u></b><br>
    •Answer: Security is maintained through cryptographic techniques, consensus mechanisms, and private keys.
</p>

    <p><u><b>10. What is blockchain's role in cryptocurrency?</u></b><br>
    •Answer: Blockchain serves as the underlying infrastructure that records and verifies all cryptocurrency transactions.
</p>

    <p><u><b>11. What are the benefits of cryptocurrencies?</u></b><br>
    •Answer: Benefits include decentralization, fast transactions, transparency, and global accessibility.
</p>

    <p><u><b>12. What risks are associated with cryptocurrencies?</u></b><br>
    •Answer: Risks include price volatility, hacking, regulatory uncertainty, and loss of private keys.
</p>

    <p><u><b>13. How do cryptocurrencies differ from digital fiat money?</u></b><br>
    •Answer: Cryptocurrencies are decentralized and trustless, while digital fiat money is issued and controlled by governments.
</p>

    <p><u><b>14. Who typically invests in cryptocurrencies?</u></b><br>
    •Answer: Retail investors, institutional investors, and technology-driven users participate in cryptocurrency markets.
</p>

    <p><u><b>15. When should individuals consider using or investing in cryptocurrencies?</u></b><br>
    •Answer: Individuals should consider cryptocurrencies when they understand the risks, technology, and regulatory environment.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencycryptocurrencytwelve(request):
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
    Capital Type: Cryptocurrency</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Cryptocurrency-based capital is best suited for early-stage through growth-stage blockchain-native projects, protocols, and digital platforms that operate within decentralized ecosystems. While some mature companies may hold or transact in cryptocurrencies, this capital model is most effective when a project has on-chain utility, network participation, or token-driven economic activity rather than purely traditional operations.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Cryptocurrency capital structures are commonly associated with blockchain foundations, DAOs, protocol entities, or hybrid on-chain/off-chain organizations. Traditional C-Corporations or LLCs may participate through token issuance, treasury holdings, or ecosystem involvement. Sole proprietorships are generally not compatible with cryptocurrency issuance at scale.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Projects utilizing cryptocurrency may have little to significant prior capital, including venture investment, grants, token presales, or ecosystem funding. Capital readiness is driven more by technical credibility, community trust, and token economics than by traditional capitalization history.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Cryptocurrency operates within the global digital asset and decentralized finance markets. Participants include retail and institutional crypto investors, exchanges, DAOs, miners or validators, and protocol users rather than traditional financial intermediaries.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital raised through cryptocurrency mechanisms can vary widely, ranging from hundreds of thousands to billions of dollars depending on token supply design, market demand, and adoption. Capital is not constrained by traditional round sizes and may be accumulated through token issuance, mining rewards, or protocol revenue.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Cryptocurrency capital does not follow traditional equity or debt rounds. Capital is typically introduced through token generation events, initial distributions, protocol launches, liquidity provisioning, or ongoing network participation rather than priced investment rounds.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Token distribution and capital release may occur over time through vesting schedules, emissions, staking rewards, or governance-approved treasury releases. Tranching is often enforced programmatically through smart contracts.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Cryptocurrency funds are commonly used for:
<br>•   Protocol development and ecosystem incentives
<br>•   Liquidity support and infrastructure costs
<br>•   Security audits and partnerships
<br>•   Community growth and on-chain governance
Use of funds may be governed by on-chain rules, multisignature controls, or decentralized governance processes.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risks include market volatility, regulatory uncertainty, custody and security risks, protocol failures, and governance disputes. Participants also face liquidity risk, token price fluctuations, and technological vulnerabilities unique to digital assets.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is reflected in token dilution, incentive emissions, governance concessions, and long-term economic trade-offs rather than interest or repayment obligations. Poorly designed token economics can materially impact long-term value.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs include protocol development, smart contract audits, legal and regulatory advisory, token design, infrastructure setup, and exchange or liquidity integration. These costs can be substantial due to technical and compliance complexity.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital can be rapid once infrastructure and market access are established, with capital inflows occurring immediately upon token launch or exchange listing. However, initial preparation, audits, and community building may take several months.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
