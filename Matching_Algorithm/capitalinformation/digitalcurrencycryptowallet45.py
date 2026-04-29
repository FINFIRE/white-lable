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

def digitalcurrencycryptowallet(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Digital Currency</b></u><br>
    Capital Type: Investment via Crypto Wallet </center></p>
    <p><b><u>Introduction</u></b><br>
Digital Currency investment via Crypto Wallets is ideal for companies and projects operating in the decentralized finance (DeFi) space or those seeking global, borderless capital with a speed and programmability that traditional fiat systems cannot match. It is designed so that a business can issue its own digital assets (tokens) or receive direct investments in established cryptocurrencies like Bitcoin (BTC) or Ethereum (ETH) to fund operations. {n} fits that definition. In 2026, "Crypto Capital" has transitioned from a niche speculative tool to an institutional asset class. Businesses now use Multi-Signature (Multi-Sig) Wallets to provide board-level governance over company funds, ensuring no single individual can move capital without authorization. On average, digital currency investments occur instantly across borders, often with transaction fees significantly lower than traditional wires. While this capital type offers 24/7 liquidity and high efficiency, the primary risk remains the extreme volatility of non-stablecoin assets and a "zero-recourse" environment; if a private key is lost or a smart contract is exploited, the capital is typically unrecoverable.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Digital Currency Investment involves the transfer of digital assets from an investor's wallet to a business's wallet. Unlike a bank transfer, this is a peer-to-peer (P2P) transaction on a public blockchain. The wallet acts as a digital "vault" that manages the cryptographic keys required to prove ownership and authorize the movement of funds. (Investopedia, 2026)
<br>


    <br>2.  The best type of companies to raise capital via crypto wallets are Web3 startups, cross-border fintechs, and asset managers looking to "tokenize" traditionally illiquid assets like real estate. In 2026, the use of Stablecoins (e.g., USDC, PYUSD) has become the primary bridge for corporate treasury, as they provide the speed of crypto without the price volatility of Bitcoin. (Deloitte, 2025)
<br>

    <br>3. The market matured significantly in late 2025 and 2026 with the passage of the GENIUS Act in the US and the full implementation of the EU's MiCA (Markets in Crypto-Assets). These laws have shifted the industry from "reactive enforcement" to "proactive compliance," allowing institutional asset managers to integrate digital assets into diversified portfolios with legal certainty. (TRM Labs, 2025)
<br>
    <br>4.While the technology is fast, it carries "custody and regulatory" risks. The "Crypto Travel Rule" (2026) requires wallet providers and intermediaries to share sender and recipient data for transactions, ending the era of anonymous high-value transfers. Furthermore, "Self-Custody" places the entire security burden on the business; losing a "Seed Phrase" or hardware wallet can result in the total loss of the investment. (InnReg, 2026)
<br>
    <br>5.
To raise capital via digital currency, a company typically issues a Token Purchase Agreement (TPA) or a SAFT (Simple Agreement for Future Tokens). Investors contribute capital to a designated wallet address. In 2026, most institutional-grade projects use Custodial Wallets provided by regulated entities like Coinbase Custody or Fidelity Digital Assets to mitigate the risks associated with manual key management. (B2BinPay, 2026)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2026). Cryptocurrency Wallets Explained: Types and Functionality. <a href="https://www.investopedia.com/terms/b/bitcoin-wallet.asp">https://www.investopedia.com/terms/b/bitcoin-wallet.asp</a>
<br>
    <br>Deloitte. (2025). Corporates Investing in Crypto: 2026 Strategy Guide. <a href="https://www.deloitte.com/us/en/services/audit-assurance/articles/corporates-investing-in-crypto.html">https://www.deloitte.com/us/en/services/audit-assurance/articles/corporates-investing-in-crypto.html</a>
<br>
    <br>TRM Labs. (2025). Global Crypto Policy Review & Outlook 2025/26. <a href="https://www.trmlabs.com/reports-and-whitepapers/global-crypto-policy-review-outlook-2025-26">https://www.trmlabs.com/reports-and-whitepapers/global-crypto-policy-review-outlook-2025-26</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   VASP Registration - Businesses acting as intermediaries must register as Virtual Asset Service Providers
<br>•   Travel Rule Compliance - Systems must be capable of transmitting PII for large transfers
<br>•   Token Classification (Howey Test) - Legal analysis required under the Digital Asset Market Clarity Act
<br>•   Form 1099-DA Reporting - Businesses must report digital asset gains and losses for tax purposes
<br>•   Anti-Money Laundering (AML) - Mandatory KYC screening for all wallet-to-wallet investment participants
<br>•   Qualified Custody - Institutional investors often legally require assets held by a regulated Qualified Custodian


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   The Project White Paper - Technically and legally reviewed disclosure of project goals
<br>•   Smart Contract Audit Report - A third-party security verification of the project's code
<br>•   Token Purchase Agreement (TPA) - The definitive legal contract for the sale
<br>•   KYC/AML Verification Records - Proof of identity for all participating investors
<br>•   Multi-Sig Governance Policy - Internal document defining who controls the wallet's private keys
<br>•   Opinion of Counsel - A legal memo classifying the asset as a commodity or security
<br>•   Proof of Reserves (PoR) - For stablecoin issuers or custodial platforms, proof that digital assets are backed 1:1

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencycryptofaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Digital Currency<br>
    Investment via Crypto Wallet</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What does investment via a crypto wallet mean?</u></b><br>
    •Answer: Investment via a crypto wallet refers to buying, holding, and managing digital currencies or tokens using a digital wallet that securely stores cryptographic keys.
</p>

    <p><u><b>2. What is a crypto wallet?</u></b><br>
    •Answer: A crypto wallet is a software or hardware tool that allows users to store, send, receive, and manage cryptocurrencies and other digital assets.
</p>

    <p><u><b>3. What types of crypto wallets are available?</u></b><br>
    •Answer: Common types include hot wallets (mobile, desktop, or web-based) and cold wallets (hardware or offline wallets).
</p>

    <p><u><b>4. How do investors fund a crypto wallet?</u></b><br>
    •Answer: Investors can fund a wallet by purchasing cryptocurrencies through exchanges or receiving transfers from other wallets.
</p>

    <p><u><b>5. What digital assets can be held in a crypto wallet?</u></b><br>
    •Answer: Crypto wallets can hold cryptocurrencies, stablecoins, NFTs, and other blockchain-based tokens, depending on wallet compatibility.
</p>

    <p><u><b>6. Is investing via a crypto wallet safe?</u></b><br>
    •Answer: Safety depends on security practices such as private key protection, two-factor authentication, and using reputable wallet providers.
</p>

    <p><u><b>7. Do crypto wallets require intermediaries like banks?</u></b><br>
    •Answer: No, crypto wallets allow direct peer-to-peer transactions without traditional banking intermediaries.
</p>

    <p><u><b>8. What are the benefits of investing through a crypto wallet?</u></b><br>
    •Answer: Benefits include user control over assets, global access, fast transactions, and transparency through blockchain technology.
</p>

    <p><u><b>9. What are the risks of investing via a crypto wallet?</u></b><br>
    •Answer: Risks include price volatility, loss of private keys, hacking, regulatory uncertainty, and lack of investor protection.
</p>

    <p><u><b>10. Can businesses invest in digital currency using crypto wallets?</u></b><br>
    •Answer: Yes, businesses can use crypto wallets for investment, payments, or treasury diversification, subject to legal and accounting rules.
</p>

    <p><u><b>11. How are returns generated from digital currency investments?</u></b><br>
    •Answer: Returns may come from price appreciation, staking rewards, yield farming, or participation in decentralized finance (DeFi).
</p>

    <p><u><b>12. Are crypto wallet investments regulated?</u></b><br>
    •Answer: Regulation varies by country, and many digital currency investments operate under evolving or limited regulatory frameworks.
</p>

    <p><u><b>13. How liquid are investments held in crypto wallets?</u></b><br>
    •Answer: Most major cryptocurrencies are highly liquid and can be traded quickly, though liquidity varies by asset.
</p>

    <p><u><b>14. Does investing via a crypto wallet dilute ownership?</u></b><br>
    •Answer: No, digital currency investments do not involve equity dilution or ownership transfer in a business.
</p>

    <p><u><b>15. When should an investor consider using a crypto wallet for investment?</u></b><br>
    •Answer: Investors may consider it when seeking alternative assets, portfolio diversification, and exposure to blockchain-based financial systems.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def digitalcurrencycryptowallettwelve(request):
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
    Capital Type: Investment via Crypto Wallet</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Digital currency investment via a crypto wallet is best suited for individual founders or businesses at any stage, as it is not tied to business maturity. It is commonly used at very early stages where traditional financing is unavailable.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
This capital type is primarily associated with individual owners, but businesses structured as LLCs or C-Corps may also hold digital assets through corporate wallets, subject to regulatory and accounting requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
No prior capital is required. The investor must already possess personal or organizational funds to convert into digital currency. There is no underwriting or third-party approval process.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
This form of capital exists within the global digital asset and cryptocurrency market, operating outside traditional banking systems and often outside conventional regulatory frameworks, depending on jurisdiction.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
There is no formal limit on capital amount, as investment size depends entirely on the individual's available funds and risk appetite. Capital deployment is fully self-directed.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Digital currency investment is not a capital round and does not involve issuing equity or debt. It represents a personal or treasury investment decision, not external fundraising.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Capital can be invested in single or multiple tranches, allowing gradual entry into the market through dollar-cost averaging or lump-sum investment strategies.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Digital assets may be used for:
<br>•   Long-term investment or speculation
<br>•   Liquidity storage outside traditional banking
<br>•   Payments (where accepted)
<br>•   Treasury diversification
Use is unrestricted but subject to volatility and legal considerations.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is very high, including price volatility, regulatory uncertainty, cybersecurity threats, loss of private keys, and lack of investor protections.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
There is no explicit cost of capital, but implicit costs include market volatility, transaction fees, exchange fees, and potential losses. There is no dilution or interest expense.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are low, typically limited to wallet setup costs, exchange fees, and transaction (gas) fees. No legal or closing costs are required.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is immediate, as funds can be converted to digital currency and accessed within minutes, depending on blockchain network speed and exchange processing.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
