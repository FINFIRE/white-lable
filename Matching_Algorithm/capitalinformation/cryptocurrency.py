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


def cryptocurrency(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Cryptocurrency</b></u></p>
    
    <p><b><u>Introduction</u></b><br>
    Cryptocurrency is an increasingly popular method for companies looking to raise capital, especially for those seeking to tap into the rapidly growing blockchain and digital asset markets. This funding model is ideal for businesses raising capital through Initial Coin Offerings (ICOs), Initial Exchange Offerings (IEOs), or Security Token Offerings (STOs), typically ranging from a few million to several hundred million dollars. Companies like {n}, particularly in the tech, blockchain, and fintech sectors, may find this an attractive option. Cryptocurrency fundraising offers a unique opportunity to sell tokens or coins to the public in exchange for capital, often appealing to investors looking for high-growth opportunities in emerging technologies. For example, in 2021, the cryptocurrency market raised over $15 billion through ICOs alone, and by 2023, the total global value of blockchain-related projects reached over $2 trillion. With average raises between $10 million and $50 million per project in 2023, this method allows businesses to quickly access capital and reach a global investor pool. Cryptocurrency fundraising is particularly suited for companies with innovative products or services that could benefit from decentralized finance (DeFi) solutions or blockchain-based applications. However, it’s important to note that this approach comes with risks, such as market volatility and regulatory uncertainty, which should be carefully considered before proceeding. There are three types of cryptocurrency option we can match you with: 1) Initial Coin Offering, 2) Initial Exchange Offering, 3) Investment Via Crypto Wallet. We will match you with apprpriate type of cryptocurrency option based on your business needs.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Cryptocurrency capital refers to the funds raised by companies or projects through the issuance of digital tokens or coins, typically via methods such as Initial Coin Offerings (ICOs), Initial Exchange Offerings (IEOs), or Security Token Offerings (STOs). These fundraising methods involve selling digital assets or tokens to investors in exchange for capital, often in the form of cryptocurrency like Bitcoin or Ethereum, or sometimes in fiat currency. Cryptocurrency capital is commonly used by blockchain-based startups or businesses involved in fintech, decentralized finance (DeFi), and other tech innovations, providing access to a global pool of investors. This method of capital raising is attractive for its speed, efficiency, and the ability to bypass traditional financial institutions, but it also comes with risks such as volatility, regulatory uncertainty, and market speculation. (Team, 2024)
<br>
    <br>2. There are several methods companies can use to raise capital through cryptocurrency, with the most common being Initial Coin Offerings (ICOs), Initial Exchange Offerings (IEOs), and Security Token Offerings (STOs). An ICO involves a company issuing a new cryptocurrency or token to investors in exchange for capital, often in the form of established cryptocurrencies like Bitcoin or Ethereum. ICOs are typically used by startups to fund blockchain-based projects, and they allow companies to reach a global audience of investors. IEOs are similar to ICOs, but they are conducted through a cryptocurrency exchange, which acts as an intermediary to offer greater trust and visibility to investors. STOs, on the other hand, involve the sale of security tokens, which are backed by real-world assets or equity, making them more compliant with regulatory standards compared to ICOs. Additionally, some companies may explore Decentralized Finance (DeFi) platforms to raise capital, which allow for peer-to-peer lending, borrowing, and liquidity pools using smart contracts. Each of these methods offers distinct advantages, including access to a global investor base, faster fundraising, and the potential for lower fees, but they also come with risks like market volatility, regulatory scrutiny, and the need for technical expertise. (Manoylov, 2024)
<br>
    <br>3. Cryptocurrency has its roots in the early 1990s when cryptographers and computer scientists began experimenting with digital money systems. The first notable attempt was DigiCash, a form of digital currency developed by David Chaum in 1990, which aimed to provide anonymous online payments. However, it was not until Bitcoin’s creation by the mysterious figure Satoshi Nakamoto in 2008 that the concept of cryptocurrency truly took off. Bitcoin was introduced as a decentralized, peer-to-peer digital currency that relied on blockchain technology to ensure secure and transparent transactions without the need for intermediaries like banks. The success of Bitcoin, which was mined for the first time in 2009, sparked the development of thousands of other cryptocurrencies, each aiming to improve upon the original model or serve niche markets. In the 2010s, cryptocurrencies gained significant attention from investors, businesses, and governments, with the rise of ICO (Initial Coin Offering) fundraising models and increasing blockchain adoption. While cryptocurrencies initially faced skepticism and regulatory challenges, by the mid-2010s, they began to be seen as a legitimate alternative asset class, and the market expanded rapidly, with a growing range of applications in finance, supply chain management, and beyond. Today, the cryptocurrency market is valued at over $2 trillion, with a wide array of tokens and blockchain innovations changing how industries function worldwide. (Ushman, 2023)
<br>
    <br>4. For companies, engaging with cryptocurrency—whether through accepting it as payment, holding it as an asset, or raising capital via crypto-based funding—introduces a range of significant risks. Market volatility is one of the most critical concerns, as the value of cryptocurrencies can fluctuate wildly in short periods, potentially impacting a company’s balance sheet. There’s also the risk of regulatory uncertainty, especially in jurisdictions where laws surrounding crypto transactions and holdings are unclear or evolving, which can result in fines, forced divestment, or reputational damage. Security threats are another major issue, as companies may be targeted by cyberattacks that compromise wallets or exchanges. Additionally, accounting and tax complexities around crypto holdings can create administrative burdens and audit complications. Companies also face potential liquidity risks, especially if they hold lesser-known tokens that cannot easily be converted to cash. Lastly, public perception and reputational risk must be considered, as association with cryptocurrency can attract scrutiny or skepticism from customers, investors, or regulators. These risks make it essential for companies to have strong internal controls, legal guidance, and risk management strategies before engaging with crypto. (Learn about the Risk of Crypto Assets. 2023)
<br>
    <br>5. To raise capital through cryptocurrency, a company must meet several technical, legal, and regulatory requirements. First, it must be a legally registered business entity, ideally in a jurisdiction with favorable crypto regulations. A comprehensive whitepaper is essential, clearly outlining the project’s purpose, technology, token structure, and business model. The company must also develop and deploy a secure blockchain-based token, often using standards like ERC-20 on Ethereum, and have its smart contract code audited to ensure investor safety. If the token qualifies as a security, the company must comply with relevant securities laws, such as those outlined by the SEC in the U.S. This may involve registering under exemptions like Reg D or Reg A+, and conducting KYC (Know Your Customer) and AML (Anti-Money Laundering) checks on all participants. A secure platform or website must be built to host the offering, communicate with investors, and facilitate transactions. Additionally, robust cybersecurity protocols and a clear legal strategy are critical to avoid fraud, protect assets, and comply with international laws. These requirements form the foundation for a legitimate and trustworthy crypto fundraising campaign. (SEC, n.d.)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Team, I. (2024, June 2). Initial Coin Offering (ICO): Coin launch defined, with examples. Investopedia. <a href="https://www.investopedia.com/terms/i/initial-coin-offering-ico.asp">https://www.investopedia.com/terms/i/initial-coin-offering-ico.asp</a>
    <br><br>Manoylov, M. (2024, August 30). Types of fundraising available to cryptocurrency projects. The Block. <a href="https://www.theblock.co/learn/286320/the-different-types-of-fundraising-available-to-cryptocurrency-projects">https://www.theblock.co/learn/286320/the-different-types-of-fundraising-available-to-cryptocurrency-projects</a>
    <br><br>Ushman, D. (2023, May 17). The history of cryptocurrencies. TrendSpider. <a href="https://trendspider.com/learning-center/the-history-of-cryptocurrencies/">https://trendspider.com/learning-center/the-history-of-cryptocurrencies/</a>
    <br><br>Learn about the Risk of Crypto Assets. (2023, October 19). Canadian Investment Regulatory Organization. <a href="https://www.ciro.ca/office-investor/understanding-risk/learn-about-risk-crypto-assets">https://www.ciro.ca/office-investor/understanding-risk/learn-about-risk-crypto-assets</a>
    <br><br>SEC.gov | Cyber, Crypto Assets and Emerging Technology. (n.d.). <a href="https://www.sec.gov/about/divisions-offices/division-enforcement/cyber-crypto-assets-emerging-technology">https://www.sec.gov/about/divisions-offices/division-enforcement/cyber-crypto-assets-emerging-technology</a>
    </p>
    <p><b><u>Qualification Requirements</u></b>
    <br>• Registered Business Entity – Must be legally incorporated (LLC, C-Corp, etc.) in a jurisdiction that permits crypto fundraising.
    <br>• Token Classification – Determine if the token is a utility or a security (using the SEC’s Howey Test if in the U.S.).
    <br>• Securities Compliance – If the token is a security, comply with regulations like Reg D, Reg A+, or Reg S, or register the offering with the SEC.
    <br>• KYC/AML Protocols – Implement Know Your Customer (KYC) and Anti-Money Laundering (AML) checks for investor verification.
    <br>• Whitepaper and Disclosures – Prepare a transparent, detailed whitepaper outlining the token, use of funds, risks, and company goals.
    <br>• Smart Contract Security – Have your smart contracts audited by reputable cybersecurity firms.
    <br>• Legal Counsel and Tax Compliance – Engage with crypto-savvy legal and tax advisors to navigate compliance and reporting.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Formation Documents – Articles of incorporation, operating agreement, and EIN/tax ID confirmation.
    <br>• Whitepaper – A comprehensive document explaining the project, technology, team, tokenomics, and fundraising goals.
    <br>• Token Offering Terms – Legal documentation that defines the token type, rights, distribution model, and fundraising structure.
    <br>• Private Placement Memorandum (PPM) – Required if the token is classified as a security, detailing the investment terms and legal disclaimers.
    <br>• KYC/AML Policy Documents – Outlining procedures to verify investor identity and comply with anti-money laundering laws.
    <br>• Legal Opinions – Third-party legal analysis classifying the token and confirming regulatory compliance.
    <br>• Smart Contract Code + Audit Reports – Verified source code and independent audit results for any token issuance contracts.
    <br>• Pitch Deck or Investor Presentation – Visual summary of the business, fundraising strategy, market opportunity, and team.
    <br>• Privacy Policy & Terms of Use – Legal documents on your website that explain how investor data is used and safeguarded.
    <br>• Marketing & Compliance Disclosures – Any promotional content must be consistent with offering terms and include legal disclaimers.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def cryptocurrencyfaq(request):
    introduction = mark_safe("""                     
    <p><b><u>FAQ's</u></b></p>
   
    <p><b><u>1. What is cryptocurrency fundraising?</u></b><br>
    • Answer: Cryptocurrency fundraising involves raising capital through the issuance and sale of digital assets like tokens or coins. This can be done through methods like ICOs (Initial Coin Offerings), IEOs (Initial Exchange Offerings), STOs (Security Token Offerings), or tokenized crowdfunding.
    </p>
                             
    <p><b><u>2. Who can raise money through cryptocurrency?</u></b><br>
    • Answer: Typically, early-stage tech startups, especially those in the Web3, DeFi, gaming, or blockchain infrastructure space. However, any company with a compelling use case and tokenomics model may explore this route, provided they meet legal and technical requirements.
    </p>
                             
    <p><b><u>3. What’s the difference between ICO, STO, and IEO?</u></b><br>
    • Answer:
    <br>• ICO: Tokens sold directly by the project team, often utility-based.
    <br>• STO: Tokens are considered securities, require compliance with SEC or local financial regulations.
    <br>• IEO: Token sale is conducted via a cryptocurrency exchange, offering built-in marketing and vetting.
    </p>
                             
    <p><b><u>4. What legal requirements must be met?</u></b><br>
    • Answer: You must:
    <br>• Choose a crypto-friendly jurisdiction (like Switzerland, Singapore, or the U.S. with legal counsel).
    <br>• Determine if your token is a security.
    <br>• Implement KYC/AML compliance.
    <br>• Draft legal documents like whitepapers, token sale agreements, and disclaimers.
    </p>
                             
    <p><b><u>5. Is raising capital via crypto legal in the U.S.?</u></b><br>
    • Answer: It can be, but it’s highly regulated. The SEC may classify your token as a security under the Howey Test. Legal counsel is essential to avoid violating securities laws.
    </p>
                             
    <p><b><u>6. What documents are required for a crypto raise?</u></b><br>
    • Answer: Common documents include:
    <br>• Whitepaper
    <br>• Pitch deck
    <br>• Tokenomics paper
    <br>• Smart contract audit report
    <br>• Legal disclaimers
    <br>• KYC/AML compliance framework
    </p>
                             
    <p><b><u><br>7. What are the risks of raising money through crypto?</u></b><br>
    • Answer: Risks include regulatory scrutiny, high volatility, smart contract bugs, investor lawsuits, exchange delistings, and reputational damage if transparency is lacking.</p>
                             
    <p><b><u>8. How long does a crypto capital raise take?</u></b><br>
    • Answer: Preparation can take 3–6 months; the sale itself can happen over days or weeks. Regulatory checks, smart contract audits, and marketing can affect this timeline.</p>
                             
    <p><b><u>9. How much can you raise through crypto?</u></b><br>
    • Answer: It varies widely. Projects have raised anywhere from $100,000 to over $100 million—but most realistic raises fall between $1 million and $10 million for early-stage companies.</p>

    <p><b><u>10. Do I need a token to raise crypto capital?</u></b><br>
    • Answer: Yes, in most cases. Tokens are what investors receive in exchange for their capital. Some Web3 grants or DAOs fund projects without equity or token demands, but these are less common for full-scale raises.</p> 
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def cryptocurrencytwelve(request):
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
    premarketStr = ''
    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'crypto fundraising would not be a viable option for raising capital.',
        'Minimum $500 - Maximum $999' :  'crypto fundraising would not be a viable option for raising capital.',
        'Minimum $1000 - Maximum $2499' :  'crypto fundraising can amplify this with leverage—but only with proper technical and legal preparation.',
        'Minimum $2500 - Maximum $4999' :  'crypto fundraising can amplify this with leverage—but only with proper technical and legal preparation.',
        'Minimum $5000 - Maximum $9999' :  'crypto fundraising can amplify this with leverage—but only with proper technical and legal preparation.',
        'Minimum $10000 - Maximum $24999' : 'crypto fundraising can amplify this with leverage—but only with proper technical and legal preparation.',
        'Minimum $25000 - Maximum $49999' : 'crypto fundraising can amplify this with leverage—but only with proper technical and legal preparation.',
        'More than $50000+' : 'crypto fundraising can amplify this with leverage—but only with proper technical and legal preparation.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'unfavourable',
        '1 Week to 2 Week' : 'unfavourable',
        '2 Weeks to 4 Weeks' : 'favourable',
        '1 Month to 2 Months' : 'favourable',
        '2 Months to 3 Months' : 'favourable',
        '3 Months to 6 Months' : 'favourable',
        '6 Months to 12 Months' : 'favourable',
        'More than 1 year' : 'favourable',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Cryptocurrency</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Cryptocurrency capital strategies—such as token pre-sales, crypto grants, or DAO-based funding—are best suited for web3-native startups with a defined technical roadmap and early community engagement. While at {stage} stage crypto startups can access non-dilutive ecosystem grants, most funding models require:
    • A whitepaper or litepaper
    • Tokenomics framework
    • Blockchain protocol selection
    • Initial development team formation
    {n} should be in the post-ideation, pre-launch phase to benefit most from crypto capital strategies, especially when planning a token issuance or dApp release.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Crypto capital access often favors decentralized or hybrid entities, but for regulatory and banking purposes, a U.S.-registered for-profit entity is still highly recommended—particularly a Delaware C-Corp or LLC with clear IP ownership and banking access.
    <br><br>If {n} is issuing a token, it may also consider forming a Foundation or DAO (offshore or otherwise) to manage governance and separation from equity-bearing entities.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    <br>If {n} has already secured {preraise} in pre-capital (from {premarketstr}), it strengthens the case for web3 participation. Crypto investors look for early traction in the form of:
    <br>• GitHub commits or open-source contributions
    <br>• A functioning testnet or MVP
    <br>• Developer or user community on Discord, Telegram, etc.
    <br>This pre-capital positioning builds trust with decentralized funders and shows proof-of-work ahead of token fundraising.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If {n}’s early capital came from {premarketstr}, layering in crypto-native funding (such as ecosystem grants, L1/L2 incentives, or token swaps) can diversify the capital stack while minimizing dilution. Bridging traditional and web3 capital positions {n} as both compliant and community aligned.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} plans to raise {raisegoal} in the next 12–18 months, it can combine:
    <br>• Ecosystem grants ($25K–$200K per blockchain protocol)
    <br>• Token presale rounds (SAFT-based, private/public, potentially raising $250K–$5M)
    <br>• DAO proposal-based funding (if building in an existing DeFi/NFT protocol ecosystem)
    <br>Token-based capital can significantly outperform equity-based rounds, but it requires strong legal structuring and transparency with future token holders.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Crypto fundraising typically follows this sequence:
    <br>1. Friends & Family or angel SAFE/SAFT
    <br>2. Private Token Round (VCs, syndicates)
    <br>3. Public Token Sale (IDO/ICO) or retroactive airdrop
    <br>4. DAO Grants / Treasury Proposals
    <br>For {n}, early participation in crypto-native rounds can offer strategic alignment with blockchain ecosystems, while equity and tokenomics can be kept separate to maximize flexibility.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Crypto capital is often released through vesting schedules tied to:
    <br>• Token launch timelines
    <br>• Milestone achievements (protocol upgrades, user growth, audits)
    <br>• DAO governance votes or multi-sig approvals
    <br> {n} should be prepared to provide clear roadmaps and token unlock schedules, especially if raising via a SAFT or launching its own token.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Crypto funding can support a variety of technical and community functions, including:
    <br>• Smart contract development and audits
    <br>• Blockchain integrations and infrastructure
    <br>• Developer incentives or bug bounties
    <br>• Community growth, marketing, and content
    <br>• Legal compliance (e.g., FinCEN, SEC, MiCA regulations)
    <br>{n} should maintain on-chain transparency for spending and prepare public dashboards or treasury tracking if accepting DAO or token-based capital.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Crypto capital strategies carry regulatory, market, and reputational risks, including:
    <br>• Token price volatility post-launch
    <br>• Legal scrutiny from U.S. regulators (e.g., SEC, CFTC)
    <br>• Community backlash or DAO governance disputes
    <br>• Technical vulnerabilities (smart contract exploits)
<br>
    <br>Risk mitigation for {n} includes:
    <br>• Engaging legal counsel with web3 expertise
    <br>• Auditing smart contracts early
    <br>• Limiting geographic exposure (e.g., blocking U.S. investors for token sales)
    <br>• Transparent, open-source development practices
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    <br>Crypto capital can be highly cost-effective, especially when sourced through:
    <br>• Non-dilutive ecosystem grants
    <br>• Airdrops and community contributions
    <br>• Staking or validator incentives
    <br>However, token-based capital (e.g., SAFT deals) often requires:
    <br>• 20%–30% of total token supply allocated to early investors
    <br>• Long vesting cliffs (12–48 months)
    <br>• Tokenomics modeling to avoid over-dilution
    <br>{n} must carefully balance token utility, investor lockups, and treasury runway to ensure long-term ecosystem growth.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    <br>Costs prior to raising crypto capital may include:
    <br>• Legal setup for token issuance (SAFT, offshore entity, ~$20K–$50K)
    <br>• Smart contract audits ($10K–$100K per audit)
    <br>• KYC/AML integration for public token sales
    <br>• Protocol fees for IDOs/launchpads (percentage of raise or flat fees)
    <br>• You can expect $1,000 to $25,000 upfront cost for raising capital before above mentioned processes.
<br>
    <br>If {n} has a {upfrontcost} allocated for development and go-to-market, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <br>Crypto capital moves fast:
    <br>• Grant programs: 2–6 weeks approval
    <br>• SAFT/token rounds: 2–8 weeks for legal + VC close
    <br>• DAO funding: 2–4 weeks via governance proposals
    <br>• Public token launches: Timeline varies by launchpad
    <br>• it could take 4-12 weeks to secure a funding.
    <br>To maximize success, {n} Company should:
    <br>• Prepare a one-pager, tokenomics doc, and technical roadmap
    <br>• Engage early with blockchain ecosystems (Solana, Base, Arbitrum, etc.)
    <br>• Build early Discord/Twitter/Telegram traction
    <br>• Secure preliminary audits or testnet feedback
    <br> {n}'s timeline is {timeanalysis} for raising capital through cryptocurrency.
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,timeanalysis=timeanalysis,premarketstr=premarketStr))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)