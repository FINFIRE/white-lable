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


def cryptocurrencyinvestmentviacryptowallet(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Cryptocurrency</b></u><br>
    Capital Type: Investments via Crypto Wallet </center></p>
    
    <p><b><u>Introduction</u></b><br>
    Crypto wallet investments are ideal for companies raising capital through tokenized assets or blockchain technology in amounts ranging from $1 million to $100 million in a given 12-month period. This method allows companies to sell digital assets directly to the public via cryptocurrency wallets, bypassing traditional intermediaries. {n} fits that definition. Crypto wallet-based investments have become a viable tool for enterprises over the past few years. For example, in the first half of 2024, over $500 million was raised through blockchain-powered token sales and crypto wallet investments. In 2023, blockchain-based offerings raised over $3.1 billion through ICO, STO, and other decentralized finance models. The total valuation of all companies raising funds via crypto wallets in early 2024 was $25 billion. On average, each crypto wallet investment offering in 2024 had a valuation of $100 million. However, investing via crypto wallets carries risks such as exposure to market volatility, potential loss of funds due to hacking or phishing attacks, and limited regulatory protection if the digital assets are not classified as securities.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1.	Cryptocurrency wallets are software applications on computers or mobile devices such as phones or tablets. They use an internet connection to access the blockchain network for the cryptocurrency you're using.
<br>
    <br>Cryptocurrencies are not "stored" anywhere—they are bits of data in a database, scattered all over it; the wallet finds all of the bits associated with your public address and sums up the amount for you in the app's interface.
<br>
    <br>Sending and receiving cryptocurrency is very easy using these applications. You can send or receive cryptocurrency from your wallet using various methods. Typically, you enter the recipient's wallet address, choose an amount to send, sign the transaction using your private key, add an amount to pay the transaction fee, and send it. (Team, 2024)
<br>
    <br>2.	Investments via crypto wallet refer to the process of allocating funds into digital assets or blockchain-based financial products using a cryptocurrency wallet as the primary tool for transacting. These wallets—such as MetaMask, Coinbase Wallet, or hardware wallets like Ledger—enable investors to securely send, receive, and store cryptocurrencies and tokens. Through this method, individuals and institutions can invest in a wide range of opportunities, including cryptocurrencies like Bitcoin and Ethereum, tokenized assets (such as real estate or equity), Initial Coin Offerings (ICOs), Security Token Offerings (STOs), decentralized finance (DeFi) protocols, and even non-fungible tokens (NFTs) when used for speculative or investment purposes. 
<br>
    <br>The defining feature of this type of investment is its blockchain-based nature and the use of a crypto wallet to directly interact with decentralized platforms, often without intermediaries. While these investments can offer accessibility, transparency, and global reach, they may also involve higher risk and varying degrees of regulatory oversight. In jurisdictions like the United States, whether these investments fall under securities regulation depends on the nature of the asset—not the method of investment. If a token or digital asset meets the criteria of an investment contract under the SEC’s Howey Test, it may be considered a security and thus subject to federal securities laws, even if it was purchased via a crypto wallet. (Team, 2024)
<br>
    <br>3.	A crypto wallet is a digital tool—software or hardware—that allows users to securely store, send, receive, and manage cryptocurrencies and other blockchain-based assets. It doesn't actually hold the coins themselves but stores the private and public keys that give users access to their crypto on the blockchain. 
<br>    There are two main types:
    <br>-	Hot wallets (connected to the internet), like MetaMask or Trust Wallet, which are more convenient but slightly more vulnerable to cyber threats.
<br>
    <br>-	Cold wallets (offline wallets), like Ledger or Trezor, which offer higher security by storing keys offline.
<br>
    <br>Crypto wallets are essential for interacting with decentralized apps (dApps), making blockchain transactions, and participating in crypto investments. (Team, 2024)
<br>
    <br>4.	Investing in cryptocurrency comes with several notable risks that investors should carefully consider. One of the most prominent is market volatility, as cryptocurrency prices can experience extreme fluctuations in short periods, resulting in significant financial gains or losses. Additionally, there are security risks, including hacking, scams, and phishing attacks. If a crypto wallet is compromised or a private key is lost, the funds may become irretrievable. Another concern is regulatory uncertainty—laws and regulations surrounding cryptocurrencies vary by country and are still evolving, which can affect trading, taxation, and legal protections. Unlike traditional investments, cryptocurrencies typically offer no investor protection, such as insurance or government backing, leaving individuals vulnerable to complete losses. There are also technology risks, such as bugs in blockchain code or smart contract errors, which can lead to malfunction or loss of funds. Finally, the industry has seen a high number of fraudulent schemes and scams, including fake projects and misleading Initial Coin Offerings (ICOs), posing an additional threat to uninformed or inexperienced investors. (FINRA, n.d.)
<br>
    <br>5.	The history of investing via cryptocurrency dates back to the launch of Bitcoin in 2009, when it became the first decentralized cryptocurrency, allowing individuals to transact directly without intermediaries like banks. Initially, cryptocurrencies were seen as a niche technological innovation, mostly used by tech enthusiasts and early adopters. As Bitcoin's value grew, along with the rise of other cryptocurrencies such as Ethereum in 2015, interest in digital asset investment began to spread beyond the crypto community. By the late 2010s, the market saw the emergence of Initial Coin Offerings (ICOs), which allowed startups to raise capital through the sale of tokens. This marked a significant shift, as it introduced the idea of tokenized investment and enabled investors to gain exposure to new blockchain projects. The crypto space exploded in popularity in 2020 and 2021, with institutional investors and large companies starting to take positions in digital currencies, further legitimizing the sector. By the mid-2020s, cryptocurrencies, decentralized finance (DeFi), and non-fungible tokens (NFTs) had become prominent investment vehicles, attracting a broader spectrum of investors, from retail to institutional. Despite challenges, including regulatory hurdles and market volatility, cryptocurrency investment has continued to evolve, drawing increasing interest from global investors seeking new opportunities in the digital economy. (Reuters, 2024)
<br>
    <br>6.	To invest via cryptocurrency, a business needs several key components in place. First, it must establish a secure crypto wallet—either a hot wallet for accessibility or a cold wallet for enhanced security—to store and manage digital assets. The business must also select a reliable cryptocurrency exchange (such as Coinbase, Binance, or Kraken) to convert fiat currency into crypto and to access various investment opportunities like Bitcoin, Ethereum, or other tokens. A solid compliance and regulatory framework is essential, especially to ensure that investments align with local laws regarding digital assets, securities, and anti-money laundering (AML) standards. Internally, the business should implement robust security protocols, including private key management, multi-signature authentication, and employee training. Lastly, a company should define clear investment goals and risk tolerance, supported by proper accounting and reporting systems for digital assets to track performance and meet tax obligations. (Maya, 2025)
    </p>
                             
    <u><b><p>References</u></b><br>
    <br>Team, I. (2024, November 25). Cryptocurrency Wallet: What it is, how it works, types, and security. Investopedia. <a href="https://www.investopedia.com/terms/b/bitcoin-wallet.asp">https://www.investopedia.com/terms/b/bitcoin-wallet.asp</a>
<br>
    <br>Crypto assets - risks. (n.d.). FINRA.org. <a href="https://www.finra.org/investors/investing/investment-products/crypto-assets/risks?">https://www.finra.org/investors/investing/investment-products/crypto-assets/risks?</a>
<br>
    <br>A timeline of Bitcoin’s wild ride to $100,000 and beyond. (2024, December). Reuters. Retrieved April 11, 2025, from <a href="https://www.reuters.com/technology/bitcoins-wild-ride-toward-100000-2024-11-21/?">https://www.reuters.com/technology/bitcoins-wild-ride-toward-100000-2024-11-21/?</a>
<br>
    <br>Maya. (2025, April 10). Crypto wallets for businesses – how to make the right choice. Synodus. <a href="https://synodus.com/blog/blockchain/crypto-wallet-for-businesses/?">https://synodus.com/blog/blockchain/crypto-wallet-for-businesses/?</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>•	Entity Structure Compliance
    <br>Must be a legally registered business (LLC, C-Corp, etc.) in good standing.
    <br>•	Corporate Governance Approval
    <br>Board or executive approval may be required (e.g., formal resolution).
    <br>•	Know Your Customer (KYC) & Anti-Money Laundering (AML)
    <br>Must comply with KYC/AML regulations for exchanges or custodians used.
    <br>•	Investment Policy Update
    <br>Internal policies must allow for digital asset investment.
    <br>•	Licensed Exchange Use
    <br>Should use registered and compliant cryptocurrency platforms (e.g., with FinCEN 	or equivalent).
    <br>•	Accounting & Tax Compliance
    <br>Adhere to IRS or local tax authority rules for reporting crypto assets and gains/losses.
    <br>•	Custodial Solutions
    <br>Must use secure and legally recognized custody solutions for holding crypto.
    <br>•	Securities Law Consideration
    <br>Must ensure tokens or coins aren’t considered unregistered securities under the SEC (Howey Test).
    <br>•	Foreign Asset Reporting (if applicable)
    <br>Companies with international operations may have to report crypto holdings under FBAR or FATCA.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>•	Business Formation Documents
    <br>Articles of Incorporation or Organization (LLC or Corp documentation)
    <br>Operating Agreement or Corporate Bylaws
    <br>•	Board Resolution or Executive Approval
    <br>A signed resolution approving crypto investments and wallet setup
    <br>•	Tax Identification Documents
    <br>Employer Identification Number (EIN) from the IRS (for U.S. companies)
    <br>Any relevant international tax ID documents
    <br>•	Investment Policy Statement
    <br>Internal policy outlining how, when, and what digital assets can be held or traded
    <br>•	Wallet Custody Agreement
    <br>Terms of service or agreements from a wallet provider or custodian (e.g., Coinbase Custody, Fireblocks, Ledger Enterprise)
    <br>•	KYC & AML Compliance Documentation
    <br>Beneficial ownership disclosures
    <br>Proof of company identity (e.g., utility bill, business license)
    <br>Identity verification of executives or authorized signers
    <br>•	Accounting & Tax Records
    <br>Purchase records and valuations for crypto assets
    <br>Crypto transaction logs (to track gains/losses)
    <br>IRS Forms (e.g., 8949, 1040 Schedule D if applicable to owners/shareholders)
    <br>•	Insurance or Risk Management Documents (Optional)
    <br>Documentation of crypto-related insurance coverage, if obtained
    </p>
        """)


    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def cryptocurrencyinvestmentviacryptowalletfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Cryptocurrency<br>
    Capital Type: Investments via Crypto Wallet</center></p>                        
    <p><center><u><b>Frequently Asked Question for Investments via Crypto Wallet</u></b></center></p>
    <p><u><b>1. What is an investment via crypto wallet, and how does it work?</u></b><br>
    • Answer: An investment via crypto wallet typically involves raising capital by offering tokens, cryptocurrencies, or digital assets in exchange for funding. These investments are managed through blockchain-based wallets, allowing investors to participate in the offering directly using digital currencies. This can be done through methods like ICOs (Initial Coin Offerings), STOs (Security Token Offerings), token sales, or DeFi fundraising.
    </p>
                             
    <p><u><b>2. Why should a company consider raising capital via crypto wallets instead of traditional methods?</u></b><br>
    • Answer: Raising capital via crypto wallets offers several benefits:
    - Global access: Crypto wallets enable businesses to attract investment from a global pool of investors.
    - Faster transactions: Capital can be raised quickly as transactions are often processed in real-time through blockchain technology.
    - Lower fees: Crypto transactions can be more cost-effective, with fewer intermediaries than traditional funding methods.
    - Increased liquidity: If you issue tokens, they can often be traded on cryptocurrency exchanges, providing liquidity for both investors and the business.
    </p>
                             
    <p><u><b>3. What types of capital-raising methods are available through crypto wallets?</u></b><br>
    • Answer: There are several ways to raise capital via crypto wallets, including:
    <br>- Initial Coin Offering (ICO): Issuing your own cryptocurrency or token to raise funds.
    <br>- Security Token Offering (STO): Issuing tokens that represent ownership in your company, regulated like traditional securities.
    <br>- Initial Exchange Offering (IEO): Raising funds through token sales hosted by an exchange.
    <br>- Decentralized Finance (DeFi) Fundraising: Creating liquidity pools or decentralized investment opportunities.
    <br>- Initial DEX Offering (IDO): A type of token sale conducted on a decentralized exchange (DEX).
    <br>- Tokenized assets or NFTs: Offering fractional ownership or unique digital assets as investment opportunities.</p>
                             
    <p><u><b>4. How quickly can I raise capital using investments via crypto wallet?</u></b><br>
    • Answer: Capital can be raised significantly faster than traditional methods, with fundraising events like ICOs, IEOs, or IDOs sometimes completing within days to weeks. However, preparation (e.g., setting up smart contracts, building a community) can take time, often requiring several months.</p>
                             
    <p><u><b>5. What are the legal and regulatory considerations when raising funds through crypto wallets?</u></b><br>
    • Answer: The regulatory environment around crypto-based fundraising varies by jurisdiction. Some key considerations include:
    <br>- Securities laws: Certain types of token offerings may be classified as securities, requiring compliance with securities regulations (e.g., registration with the SEC in the U.S.).
    <br>- AML/KYC requirements: Anti-money laundering and Know-Your-Customer protocols may need to be implemented to verify the identity of investors.
    <br>- Jurisdictional differences: Regulations vary across regions, so you may need legal advice to ensure compliance in multiple jurisdictions.
    </p>
                             
    <p><u><b>6. What are the costs involved in raising capital via crypto wallets?</u></b><br>
    • Answer: The costs can include:
    <br>- Legal and regulatory compliance: Legal fees for drafting documents and ensuring compliance with securities laws.
    <br>- Technology and platform development: Building and securing the infrastructure (blockchain, smart contracts) to handle crypto transactions.
    <br>- Marketing and community building: Promoting your offering to attract investors.
    <br>- Exchange and listing fees: Fees for listing tokens on centralized or decentralized exchanges.
    <br>- Transaction fees: Fees associated with transferring tokens or converting crypto assets.
    </p>
                             
    <p><u><b>7. What are the potential risks of raising funds through crypto wallets?</u></b><br>
    • Answer: Some of the risks include:
    <br>- Market volatility: Cryptocurrencies can be highly volatile, which can affect the value of funds raised or the price of your token.
    <br>- Regulatory uncertainty: The evolving regulatory landscape around crypto fundraising may impact the long-term viability of your offering.
    <br>- Security risks: The risk of hacking, fraud, or loss of funds in crypto wallets or exchanges.
    <br>- Liquidity challenges: Depending on the type of token issued, there may be challenges in converting crypto assets to fiat currency quickly.</p>
                             
    <p><u><b>8. What type of investors typically participate in crypto-based capital raising?</u></b><br>
    • Answer: Investors in crypto-based fundraising typically include:
    <br>- Retail investors: Individuals who are familiar with cryptocurrencies and decentralized technologies.
    <br>- Venture capitalists: Some VCs are increasingly participating in the crypto space, especially in projects with strong technology and community backing.
    <br>- Institutional investors: Larger entities that may invest in security token offerings (STOs) or blockchain-focused funds.
    <br>- Crypto enthusiasts: Individuals who believe in the potential of your project or the technology behind it, often looking for long-term gains.
    </p>
                             
    <p><u><b>9. Do I need technical expertise to raise capital via crypto wallets?</u></b><br>
    • Answer: Yes, some level of technical expertise is required, especially if you are building your own blockchain or token. You'll need to work with developers to:
    <br>- Create and audit smart contracts.
    <br>- Ensure the security of your platform and wallets.
    <br>- Integrate with exchanges or DeFi platforms.
    <br>- Handle any token issuance and tokenomics setup. However, many businesses partner with external blockchain development firms or consultants to handle the technical side.</p>
                             
    <p><u><b>10. How can I ensure the security of the funds raised through crypto wallets?</u></b><br>
    • Answer: Ensuring the security of your funds is critical. Some steps include:
        <br>- Auditing smart contracts to identify vulnerabilities before they are deployed.
        <br>- Using multi-signature wallets to protect funds from unauthorized access.
        <br>- Implementing security measures such as encryption, cold storage, and regular system audits.
        <br>- Engaging third-party security firms for penetration testing and advice on best practices.</p>
                             
    <p><u><b>11. What are the benefits of issuing tokens versus equity when raising capital via crypto wallets?</u></b><br>
    • Answer: Issuing tokens allows for greater liquidity, as tokens can be traded on exchanges. It also offers more global accessibility for investors. On the other hand, equity involves offering actual ownership in the company and may provide investors with voting rights and dividends. The decision between tokens and equity depends on the nature of your project, your goals, and the level of regulatory compliance you're willing to pursue.</p>
                             
    <p><u><b>12. What is the difference between an ICO, STO, and IDO?</u></b><br>
    • Answer:         
    <br>- ICO (Initial Coin Offering): A fundraising method where a company issues its own cryptocurrency or tokens in exchange for capital, typically in a more unregulated environment.
    <br>- STO (Security Token Offering): A regulated offering where tokens are classified as securities and must comply with securities laws, offering investors legal protections and ownership rights.
    <br>- IDO (Initial DEX Offering): A type of token sale conducted on a decentralized exchange (DEX), which allows for immediate trading and liquidity once the tokens are issued.
    </p> 
                             
    <p><u><b>13. How do I set the value of my token, and what is its utility?</u></b><br>
    • Answer: The value of your token will depend on:
    <br>- Tokenomics: This includes the supply, demand, and utility of your token within your ecosystem.
    <br>- Market demand: The perceived value of your token in relation to similar offerings in the market.
    <br>- Use case: Your token should have real utility within your platform or product (e.g., as a payment method, access to features, governance rights, etc.).
    <br>- Price strategy: You can set an initial price based on the value proposition of your token, with the possibility of it appreciating over time.</p>

    <p><u><b>14. How do I ensure transparency and trust in the process?</u></b><br>
    • Answer: Transparency is key to gaining the trust of your investors:
        <br>- Whitepaper: Provide a clear, detailed whitepaper outlining your project, tokenomics, business plan, and technical specifications.
        <br>- Regular updates: Keep investors informed with frequent project updates, progress reports, and milestones.
        <br>- Third-party audits: Use reputable firms to audit your smart contracts and platform to show that your project is secure and trustworthy.</p>
    
     <p><u><b>15. Can I raise funds through crypto wallets if I’m a traditional business or non-tech startup?</u></b><br>
    • Answer: Yes, many traditional businesses are exploring crypto-based fundraising, especially as crypto adoption grows. However, it's essential to understand the technology and engage with the right technical and legal partners to successfully integrate crypto wallets into your business model.</p>           
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def cryptocurrencyinvestmentviacryptowallettwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR</b></u><br>
    Capital Type: Investments via Crypto Wallet</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    For a company using crypto wallets for investment purposes, the ideal stage of development depends on the company’s goals. However, it generally becomes more ideal once the company reaches the growth phase and is working towards scalability and compliance while managing more complex crypto financial products and systems. Early-stage companies might use crypto wallets for fundraising or niche purposes, but the full potential is realized as the business matures, focusing on broader crypto-based services and institutional partnerships.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The LLC is often the best choice for smaller or mid-sized companies in the early to growth stages of using crypto wallets for investment purposes due to its flexibility, limited liability protection, and tax advantages. However, for businesses looking to scale, raise significant investment, or cater to institutional investors, a Corporation (C-Corp) or Limited Partnership (LP) might be more suitable.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    There are no universal restrictions specifically tied to businesses that have raised a certain amount of pre-capital before using investments via a crypto wallet, however, significant regulatory and compliance considerations exist. These include adhering to securities laws, AML/KYC requirements, and tax reporting obligations. 
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    There are no blanket rules that prevent companies from using crypto wallets for investments after raising pre-capital, certain restrictions may apply depending on the type of capital raised, jurisdiction, and regulatory compliance. These restrictions typically revolve around securities laws, AML/KYC requirements, tax obligations, and investor protections. If a company has raised significant capital through ICOs, token sales, or traditional equity rounds, it must carefully navigate regulatory and legal frameworks to ensure it complies with these requirements when using crypto wallets for further investments.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    There is no strict upper limit to how much a company can raise using investments via a crypto wallet. Companies have raised anywhere from millions to billions of dollars. However, the total amount a company can raise is often determined by the regulatory environment, the type of offering, and the legal compliance required. While some crypto fundraising methods allow for large sums to be raised, compliance with local and international laws (including securities regulations, KYC/AML, and tax requirements) is essential for a successful and legal fundraising campaign.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The pre-seed and seed rounds are the best fit for a company seeking to use crypto wallets to raise capital. These rounds are characterized by flexibility, early-stage capital raising, and a focus on innovative funding mechanisms, such as token sales, crowdfunding via crypto wallets, or other blockchain-based solutions.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    The number of tranches when raising capital through crypto wallets depends on the company’s fundraising structure, strategy, and regulatory considerations. While there's no strict limit, a typical model involves anywhere from 2 to 5 tranches (e.g., pre-sale, main sale, milestone tranches). The most suitable model will depend on the project’s goals, the type of investors targeted, and the legal and technical frameworks in place.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A business can generally use funds raised via crypto wallets for purposes such as product development, marketing, operational expenses, hiring, expansion, and compliance.  
    <br>Restrictions:
    <br>• Legal and Regulatory Compliance: Must adhere to securities regulations (for STOs or tokens considered securities), AML/KYC laws, and tax obligations.
    <br>• Investment Terms: Funds may be tied to specific milestones, project goals, or investor agreements, especially in token sales or security token offerings.
    <br>• Investor Protections: Some agreements might restrict fund usage to protect investor interests (e.g., milestone-based funding or purpose-specific spending).
    <br>• Transparency and Accountability: To maintain investor trust and regulatory compliance, businesses are often required to report on the use of proceeds and ensure the funds are allocated according to the disclosed plan.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    When a business decides to raise capital via crypto wallets, the level of risk tolerance required is generally higher compared to traditional investment methods. This is because the world of cryptocurrency and blockchain technology comes with unique challenges and risks. These risks are driven by factors such as volatility, regulatory uncertainty, and the evolving nature of the crypto space. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The level of capital cost tolerance required for a business to use investments via crypto wallets depends on the specific type of offering, the scale of the project, and the complexity of the technology involved. However, moderate to high capital cost tolerance is generally necessary due to; legal and regulatory compliance requirements, technology infrastructure and security measures, marketing and community-building costs and exchange and platform fees.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Smaller projects with basic offerings (e.g., using an existing blockchain platform, limited marketing, and straightforward legal advice) may incur upfront costs as low as $50,000 to $100,000. Larger projects, especially those that are more complex in terms of technology, legal compliance, marketing, and exchange listing, may see costs ranging from $200,000 to $1,000,000 or more in upfront expenditures.

    <br><br>It's important to note that the level of complexity, size of the fundraising, and market strategy can dramatically affect these figures. If a business is new to the crypto space, it is prudent to budget more for legal compliance and marketing, as these areas often require specialized expertise and careful planning.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Fastest Fundraising methods are IDOs, DeFi liquidity pools, and IEOs that allow companies to raise capital within a few days to a month once the offering is launched.
    <br>Longer Fundraising methods are ICO/STO/token sales or private rounds that might take several weeks to months for full fundraising, depending on preparation, interest, and market conditions.
    <br>While the capital raising process using crypto wallets can be quite fast compared to traditional methods, the time spent preparing the project (legal setup, community-building, technical infrastructure) is crucial for ensuring success.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)