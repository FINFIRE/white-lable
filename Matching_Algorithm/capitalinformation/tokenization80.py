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


def tokenization(request):
    introduction = mark_safe("""
    <p><b><u>Capital Market: Tokenization</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Tokenization is ideal for companies seeking to raise capital or improve asset liquidity by converting real-world assets—such as equity, debt, real estate, or revenue rights—into digital tokens on a blockchain. {n} fits this model, particularly if it aims to modernize asset management, enhance investor accessibility, and support fractional ownership. Tokenization has gained traction over the past 5–7 years, particularly with the rise of regulated platforms such as Securitize and tZERO. For example, by 2024, the global tokenized asset market was estimated to surpass $2.3 billion in value, with forecasts projecting a rise to $16 trillion by 2030. In 2023 alone, security token offerings (STOs) globally raised over $500 million across various sectors including real estate, venture capital, and private equity. On average, tokenized equity offerings in 2023 ranged in valuation between $10 million and $100 million, depending on the asset class and jurisdiction. While tokenization offers transparency, liquidity, and democratized access to investments, it also carries risks such as regulatory uncertainty, platform security vulnerabilities, and lower secondary market activity.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Tokenization is the process of converting real-world assets or ownership rights—such as real estate, equity, or other valuable items—into digital tokens that exist on a blockchain. These tokens represent a share of the underlying asset and are tradable on decentralized platforms, allowing for fractional ownership, increased liquidity, and broader access to investors. Tokenization can be applied to various asset classes, including securities, commodities, and even intellectual property, enabling more efficient and transparent transactions. The process typically involves the creation of a digital representation (a token) that is backed by the asset, making it easier to buy, sell, or transfer ownership. (Hayes, 2024)
<br>
    <br>2. Tokenization involves the process of converting sensitive data or assets into digital tokens, which can be securely used in various applications, especially in data security, asset management, and payments. In data tokenization, sensitive information such as credit card numbers or personal data is replaced with a randomly generated token that has no value on its own. The original data is securely stored in a tokenization vault, accessible only through authorized systems, preventing exposure during transactions. Asset tokenization, often used in the context of blockchain, involves converting physical or digital assets like real estate or stocks into digital tokens. These tokens represent fractional ownership or rights to the asset and can be easily traded on secondary markets, offering liquidity to assets that were previously illiquid. This process includes identifying the asset, issuing tokens on a blockchain, and ensuring legal backing for the tokenized assets. Lastly, in payment tokenization, payment data like credit card numbers is replaced with tokens during financial transactions, ensuring that sensitive data is never exposed to the network and reducing fraud risk.
<br>
    <br>These types of tokenization phases enhance security, efficiency, and liquidity across various industries. Data tokenization ensures that sensitive information is protected, while asset and payment tokenization enable the fractionalization and secure transfer of value in both traditional and digital economies. (Robertson, 2023)
<br>
    <br>3. Tokenization has evolved over time, originating in the realm of data security before expanding into various sectors, including finance, real estate, and digital assets. The concept began in the 1970s when financial institutions developed basic tokenization systems to secure sensitive information during transactions, such as credit card details. Initially used in payment systems to reduce fraud risks, tokenization replaced sensitive data with randomly generated tokens that had no intrinsic value. As blockchain technology emerged in the late 2000s, tokenization found a new application in the representation of real-world assets, leading to the development of asset tokenization. This allowed tangible and intangible assets, including property, stocks, and intellectual property, to be digitized and traded on decentralized platforms. By the 2010s, with the rise of blockchain, the tokenization of financial assets became more mainstream, paving the way for innovations in decentralized finance (DeFi) and non-fungible tokens (NFTs). Today, tokenization continues to gain traction in various industries as a means of enhancing security, liquidity, and accessibility. (Hayes, 2024)
<br>
    <br>4. Tokenization offers numerous benefits but also comes with a range of risks. One significant concern is regulatory uncertainty, as the technology is still relatively new and lacks clear, standardized regulations, creating legal ambiguities for businesses and investors. Additionally, tokenization's reliance on digital platforms exposes it to cybersecurity risks, including hacking and data breaches, which could result in financial loss or stolen tokens. Smart contract vulnerabilities also pose a threat, as poorly coded contracts can be exploited, leading to security breaches. Market volatility is another risk, as tokenized assets can experience fluctuations in value, making them more unpredictable than traditional investments. Liquidity concerns may arise if there is insufficient demand or an underdeveloped market infrastructure, potentially hindering the ease of buying or selling tokenized assets. Furthermore, tokenized assets may not offer the same level of investor protection as traditional securities, leaving investors more exposed to fraud or financial losses. Finally, the heavy reliance on blockchain technology introduces a risk of system failure, which could disrupt the entire tokenization process. These risks should be carefully considered when engaging in tokenization, and adequate safeguards must be implemented to mitigate potential issues. (Finextra, 2024)
<br>
    <br>5. To use tokenization, businesses must ensure they meet legal and regulatory requirements, including compliance with securities laws and engaging legal counsel for ownership and liability issues. They need to develop or hire experts to create secure smart contracts, which are self-executing agreements that facilitate token issuance and transactions. A blockchain platform, such as Ethereum or Binance Smart Chain, is essential for managing tokenized assets securely and efficiently. Businesses must define the type of token they wish to create, such as a security or utility token, and design an economic model for its utility and liquidity. Strong cybersecurity measures are crucial to prevent hacking and fraud, along with transparent asset valuations for investor confidence. Many businesses partner with tokenization platforms to handle token creation, compliance, and management. Additionally, secure custody services, investor education, and clear communication are important, particularly for offering transparency to those new to tokenized assets. If tokens are tradable, businesses should ensure the necessary infrastructure for liquidity and trading, including exchanges or secondary markets. By addressing these elements, businesses can successfully implement tokenization while ensuring compliance, security, and efficiency in managing digital assets. (Hayes, 2024).
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Hayes, A. (2024, April 5). What is tokenized equity? How tokenized stock works, and examples. Investopedia. <a href="https://www.investopedia.com/terms/t/tokenized-equity.asp">https://www.investopedia.com/terms/t/tokenized-equity.asp</a>
    <br>Robertson, B. (2023, December 20). What is Tokenization | Data & Payment Tokenization Explained | Imperva. Learning Center. <a href="https://www.imperva.com/learn/data-security/tokenization/?">https://www.imperva.com/learn/data-security/tokenization/?</a>
    <br>Asset tokenization: Digital assets explained | Chainlink. (n.d.). <a href="https://chain.link/education/asset-tokenization?">https://chain.link/education/asset-tokenization?</a>
    <br>Finextra. (2024, October 22). The Hidden Dangers of Tokenization: What You Need To Know: by Alexander Boehm. Finextra Research. <a href="https://www.finextra.com/blogposting/27065/the-hidden-dangers-of-tokenization-what-you-need-to-know?">https://www.finextra.com/blogposting/27065/the-hidden-dangers-of-tokenization-what-you-need-to-know?</a>
    </p>
    
    <p><b><u>Qualification Requirements</u></b>
    <br>• Securities Laws Compliance: Security tokens must adhere to securities regulations, which may include registration or exemptions.
    <br>• AML/KYC Compliance: Businesses must verify investor identities and ensure funds are legitimate to prevent fraud.
    <br>• Legal Entity: The business must be a legally recognized entity (e.g., corporation or LLC).
    <br>• Token Classification: Determine whether tokens are securities (regulated) or utility tokens (fewer regulations).
    <br>• Jurisdictional Compliance: Ensure compliance with local and international regulations, especially for cross-border offerings.
    <br>• Documentation: Legal documents like offering memorandums or prospectuses are required, especially for security tokens
    <br>• Smart Contract Legality: Ensure smart contracts are enforceable and legally sound.
    <br>• Consumer Protection: Provide clear terms and disclosures to investors, with mechanisms for dispute resolution.
    <br>• Tax Considerations: Understand tax obligations for both the company and investors.
    <br>• Ongoing Compliance: Maintain reporting obligations and ongoing regulatory compliance post-offering.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Offering Memorandum or PPM: A document outlining the terms, risks, and rights of token holders, especially for security tokens.
    <br>• Token Issuance Agreement: A legal contract detailing the terms of the token sale between the business and investors.
    <br>• Prospectus: If applicable, a filing with regulatory authorities containing detailed information about the offering.
    <br>• Business Plan or Executive Summary: A document outlining the company’s strategy, market opportunity, and financial projections.
    <br>• Token Whitepaper: Required for utility tokens, explaining the token's purpose, functionality, and value proposition.
    <br>• Smart Contract Code and Audit Reports: The code governing the token sale, accompanied by a third-party audit for security and compliance.
    <br>• AML and KYC Policies: Procedures for verifying investor identities and ensuring compliance with anti-money laundering regulations.
    <br>• Securities Filings or Exemptions: Documentation related to securities law compliance or any exemptions the offering may qualify for.
    <br>• Financial Statements and Audited Reports: Audited financials demonstrating the business’s financial health and transparency.
    <br>• Legal Opinion Letter: A letter from legal counsel confirming compliance with applicable laws and regulations.
    <br>• Risk Disclosure Statement: A document outlining the risks involved with the token offering, ensuring investor awareness.
    <br>• Token Sale Terms and Conditions: The detailed rules and conditions governing the token sale, including pricing and eligibility.
    <br>• Investor Accreditation Forms: Forms to verify that investors meet required eligibility criteria, such as accredited investor status.
    <br>• Subscription Agreement: A contract formalizing the investor’s commitment to purchasing tokens.
    <br>• Post-Offering Disclosure and Reporting Forms: Ongoing reporting obligations to keep investors informed after the offering.
    <br>• Tax Documentation: Necessary forms to ensure tax compliance related to the token issuance and sale.
    <br>• Token Distribution Plan: A plan detailing how tokens will be allocated among stakeholders, including vesting schedules.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def tokenizationfaq(request):
    introduction = mark_safe("""
    <p><b><u>FAQs</u></b></p>                        
                             
    <p><b><u>1. What is tokenization, and how does it work?</u></b><br>
    • Answer: Tokenization involves creating digital tokens on a blockchain that represent ownership of assets or equity in a business. These tokens can be bought, sold, or traded by investors. It allows businesses to digitize real-world assets or equity and raise capital by offering tokens in exchange for investment.
    </p>
                             
    <p><b><u>2. What are the advantages of using tokenization for raising capital?</u></b><br>
    • Answer: Tokenization offers several advantages, including:
    <br>- Global Access: Tokens can be sold to investors worldwide, removing geographical barriers.
    <br>- Liquidity: Tokenized assets can be traded on secondary markets, potentially increasing liquidity compared to traditional investments.
    <br>- Transparency and Security: Blockchain technology ensures transparent, immutable records of ownership and transactions, reducing fraud risks.
    <br>- Fractionalization: Tokenization allows businesses to sell fractionalized ownership, making investments more accessible to smaller investors.
    <br>- Cost Efficiency: Tokenization can lower administrative and transaction costs compared to traditional capital raising methods like IPOs or private equity rounds.</p>
                             
    <p><b><u>3. How is tokenization different from traditional capital-raising methods (e.g., IPOs or venture capital)?</u></b><br>
    • Answer: Traditional capital-raising methods like IPOs and venture capital typically require extensive paperwork, long timelines, and significant fees for legal, underwriting, and exchange listing costs. Tokenization, by contrast, leverages blockchain technology to streamline the fundraising process, often reducing intermediaries and providing more direct access to a global pool of investors.</p>
                             
    <p><b><u>4. What types of tokens can a business issue?</u></b><br>
    • Answer: There are generally two main types of tokens businesses issue:
    <br>- Security Tokens: These represent ownership in a company or asset and are subject to securities regulations. They offer the rights to dividends, profits, or voting power and can be traded on approved exchanges.
    <br>- Utility Tokens: These are typically used within a particular platform or ecosystem to access goods or services. They are not considered securities and are generally subject to fewer regulatory requirements.</p>
                             
    <p><b><u>5. What legal and regulatory considerations do I need to be aware of when using tokenization?</u></b><br>
    • Answer: The primary legal considerations include:
    <br>- Securities Laws: If you are issuing security tokens, they are likely subject to securities laws (e.g., SEC regulations in the U.S.). This requires legal documentation and possibly filings with regulatory bodies.
    <br>- KYC/AML Compliance: Companies need to implement Know Your Customer (KYC) and Anti-Money Laundering (AML) processes to verify investor identities and ensure compliance.
    <br>- Jurisdictional Variability: Regulations vary by jurisdiction, so you need to be aware of the legal environment in each country where you plan to raise capital.
    </p>
                             
    <p><b><u>6. How much capital can I raise using tokenization?</u></b><br>
    • Answer: The amount of capital you can raise depends on the size of the offering, the type of tokens issued, and investor demand. Tokenization can be used for small-scale fundraising (e.g., tens of thousands of dollars) to large-scale efforts (millions of dollars), depending on your needs and the market interest.</p>
                             
    <p><b><u>7. How long does it take to raise capital through tokenization?</u></b><br>
    • Answer: The process of tokenization typically takes 3 to 6 months, but it can vary based on the complexity of the offering and regulatory requirements. This includes time for legal and regulatory preparation, technology setup (such as smart contracts and blockchain infrastructure), marketing, and investor engagement.</p>
                             
    <p><b><u>8. What are the costs associated with tokenization?</u></b><br>
    • Answer: The upfront costs for tokenization can range from $200,000 to $500,000 or more, depending on the complexity of the project. These costs include blockchain development, legal fees, smart contract audits, marketing campaigns, and regulatory compliance costs. Businesses should also be prepared for ongoing costs related to token management, governance, and liquidity maintenance.</p>
                             
    <p><b><u>9. How can tokenized assets or equity be traded or transferred?</u></b><br>
    • Answer: Tokenized assets or equity can be traded on digital asset exchanges or private trading platforms. Depending on the structure, security tokens may only be traded on approved exchanges, while utility tokens might have more flexible trading options. It’s important to ensure that the tokens are listed on an exchange or platform that allows investors to buy, sell, or transfer their tokens post-offering.</p>
                             
    <p><b><u>10. What are the risks associated with using tokenization?</u></b><br>
    • Answer: While tokenization has many benefits, there are also risks, including:
    <br> Regulatory Risk: The legal landscape for tokenization is evolving, and regulatory changes could impact your offering or future operations.
    <br> Technology Risk: Blockchain and smart contract vulnerabilities can expose the company and its investors to cyber threats.
    <br> Market Risk: The value of tokens can fluctuate based on market demand, which might impact your ability to raise funds or achieve liquidity.
    <br> Liquidity Risk: Although tokenized assets can theoretically be traded, secondary market liquidity may not be guaranteed, especially if the token does not attract sufficient investor interest.</p>
                             
    <p><b><u>11. Can I use tokenization to raise funds from both institutional and retail investors?</u></b><br>
    • Answer: Yes, tokenization can enable businesses to access both institutional investors (e.g., venture capital firms, hedge funds) and retail investors (individuals) globally. However, depending on the type of token and jurisdiction, you may need to ensure that certain compliance measures (such as accredited investor requirements) are met for specific groups.</p>
                             
    <p><b><u>12. Do I need to have an existing blockchain-based business to use tokenization?</u></b><br>
    • Answer: No, you do not need to have a blockchain-based business to use tokenization. Tokenization can be applied to any business or asset that can be represented digitally. Many companies from various industries (real estate, finance, art, etc.) use tokenization to raise capital without being involved in blockchain-based services.
    </p> 
                             
    <p><b><u>13. How does tokenization compare to equity crowdfunding or ICOs?</u></b><br>
    • Answer: Tokenization offers some key advantages over traditional equity crowdfunding or Initial Coin Offerings (ICOs):
    <br> Security: Tokenized equity can be structured as security tokens, offering ownership rights and legal protections, unlike utility tokens in ICOs that may not confer ownership.
    <br> Regulatory Compliance: Tokenization, especially with security tokens, is often subject to more established regulatory frameworks, providing greater legal protection for both the company and investors, compared to the often unregulated nature of ICOs.
    <br> Liquidity: Security tokens can be listed on secondary markets, offering more liquidity than typical crowdfunding investments.</p>

    <p><b><u>14. What are the benefits of fractionalizing assets through tokenization?</u></b><br>
    • Answer: Fractionalizing assets means breaking up large, valuable assets (e.g., real estate or fine art) into smaller, affordable tokens. This opens up investment opportunities to a broader range of investors, lowers the entry barrier for those who might not afford full ownership, and provides more flexibility for asset management and liquidation.</p>
    
    <p><b><u>15. How do I ensure that my tokenization project is successful?</u></b><br>
    • Answer: Success in tokenization requires:
    <br>- Clear value proposition: Ensure that your token offering provides real value to investors.
    <br>- Effective marketing: Engage with potential investors early through targeted marketing campaigns and community-building efforts.
    <br>- Legal compliance: Work with legal experts to ensure compliance with all relevant securities laws and regulations.
    <br>- Strong security practices: Invest in secure blockchain infrastructure and regular audits to ensure investor confidence.
    <br>- Post-offering support: Maintain transparency and provide investor updates to build trust and ensure long-term success.</p>           
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def tokenizationtwelve(request):
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
    
    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'Cost below $499 is limited for the deal and, you may consider starting with a private tokenized raise under Reg D or Reg S and scaling up later.',
        'Minimum $500 - Maximum $999' : 'Cost below $999 is limited for the deal and, you may consider starting with a private tokenized raise under Reg D or Reg S and scaling up later.',
        'Minimum $1000 - Maximum $2499' : 'Cost below $2499 is limited for the deal and, you may consider starting with a private tokenized raise under Reg D or Reg S and scaling up later.',
        'Minimum $2500 - Maximum $4999' : 'Cost below $4999 is limited for the deal and, you may consider starting with a private tokenized raise under Reg D or Reg S and scaling up later.',
        'Minimum $5000 - Maximum $9999' : 'Cost between $5000 and $9999 is generally enough for the deal and, you may consider scaling up later with additional cost.',
        'Minimum $10000 - Maximum $24999' : 'Cost between $10000 and $24999 is generally enough for the deal and, you may consider scaling up later with additional cost.',
        'Minimum $25000 - Maximum $49999' : 'Cost between $25000 and $49999 is generally enough for the deal and, you may consider scaling up later with additional cost.',
        'More than $50000+' : 'Cost over $50000 is generally enough for the deal and, you may consider scaling up later with additional cost.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'completing the entire process within a 1 day to 1 week timeframe presents significant challenges on completing the raise.',
        '1 Week to 2 Week' : 'While completing it within your time period of 1-2 weeks is difficult; depending on legal readiness, smart contract development, and investor onboarding. Compared to traditional equity, this timeline can be faster due to programmable automation—but only if compliance and infrastructure are pre-prepared.',
        '2 Weeks to 4 Weeks' : 'While completing it within your time period of 2-4 weeks is difficult; depending on legal readiness, smart contract development, and investor onboarding. Compared to traditional equity, this timeline can be faster due to programmable automation—but only if compliance and infrastructure are pre-prepared.',
        '1 Month to 2 Months' : 'depending on legal readiness, smart contract development, and investor onboarding. Compared to traditional equity, this timeline can be faster due to programmable automation—but only if compliance and infrastructure are pre-prepared.',
        '2 Months to 3 Months' : 'depending on legal readiness, smart contract development, and investor onboarding. Compared to traditional equity, this timeline can be faster due to programmable automation—but only if compliance and infrastructure are pre-prepared.',
        '3 Months to 6 Months' : 'depending on legal readiness, smart contract development, and investor onboarding. Compared to traditional equity, this timeline can be faster due to programmable automation—but only if compliance and infrastructure are pre-prepared.',
        '6 Months to 12 Months' : '6 months to 12 months provides sufficient time to execute the full capital raise.',
        'More than 1 year' : 'A 12+ month horizon provides sufficient time to execute the full capital raise.',             
    }

    timeanalysis = up_front_time_options[upfronttime]

    premarketStr = ''
    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Tokenization</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As {n} enters its {stage} stage, tokenization offers a modern and flexible method of raising capital by issuing digital tokens that represent equity, debt, or asset-backed securities. Tokenized securities are ideal for companies that have a solid technological foundation, traction in the market, and seek to diversify funding sources beyond traditional private equity or venture capital. This method allows fractional ownership and global investor access, which can accelerate fundraising and liquidity options.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Tokenization is best suited for {entity} or entities that can support a compliant equity or debt issuance structure. For {n}, which is structured as a {entity}, issuing tokenized securities (such as equity tokens or revenue-sharing tokens) is feasible and can be aligned with U.S. securities regulations (e.g., Reg D, Reg A+, Reg S). The cap table must be equipped to handle digital asset representation, typically through smart contract infrastructure.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} in pre-capital already secured, {n} demonstrates momentum and investor interest—critical for building confidence in a tokenized capital raise. Pre-capital validation is especially important in token offerings, where transparency, trust, and community support are key. It also makes {n} more attractive to blockchain-native investors seeking equity or asset exposure via compliant digital tokens.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Given this financial foundation, tokenization allows {n} to access a broader, often global, investor pool—especially those familiar with Web3, DeFi, or fintech ecosystems. Digital securities are appealing to both institutional and accredited investors who desire transparency, fast settlement, and potential liquidity through regulated secondary trading platforms.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} plans to raise {raisegoal}, tokenization offers a streamlined, programmable method of issuance, often at lower costs compared to traditional methods. However, the company must clearly define token structure, rights (e.g., dividends, voting), and compliance pathways. Investors will expect a clear tokenomics model, a transparent cap table, and a compliant offering framework.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Tokenized securities can be structured as early-stage Seed or Series A offerings but are most commonly aligned with growth-stage raises where traction has been established. For {n}, a tokenized capital round can serve as an alternative or supplement to traditional Series A/B, especially if the company is tech-forward or involved in the digital asset space.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Tokenized capital raises can be distributed in tranches through smart contracts, released upon achievement of specific milestones such as product development, user growth, or revenue benchmarks. This model enhances investor trust and supports founder control by ensuring capital is unlocked based on performance.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Capital raised through tokenization can fund:
    <br>- Technology development
    <br>- User acquisition
    <br>- Decentralized infrastructure
    <br>- Compliance and regulatory readiness
    <br>- Liquidity provisioning (if tokens are meant for secondary trading)
    <br>Clear use-of-funds documentation and milestone tracking are crucial to meet investor expectations and legal obligations.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Tokenized offerings carry regulatory, technical, and market risks, often higher than traditional equity. {n} must ensure robust compliance, smart contract audits, and investor education to mitigate risk. However, investors familiar with Web3 and digital assets often understand and embrace this trade-off in exchange for innovation and potential liquidity.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The cost of tokenized capital is generally lower than venture or private equity in terms of dilution—especially if structured creatively (e.g., revenue-based tokens or convertible digital notes). However, regulatory compliance, smart contract development, and platform fees can still represent significant upfront and ongoing costs.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront cost to structure and launch a tokenized securities offering typically ranges from $1,000 to $15,000, depending on legal jurisdiction, smart contract complexity, and whether {n} uses a white-label platform or builds in-house. If {n}’s {upfrontcost} is limited, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Tokenized capital raises can be completed in 4–12 weeks, {timeanalysis}
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,timeanalysis=timeanalysis))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)