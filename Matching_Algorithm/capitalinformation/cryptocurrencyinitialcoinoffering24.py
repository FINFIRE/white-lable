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


def cryptocurrencyinitialcoinoffering(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Cryptocurrency</b></u><br>
    Capital Type: Initial Coin Offering</center></p>
    <p><b><u>Introduction</u></b><br>Over 2,000 ICOs were launched for a total of $8.7 billion raised in 2024, with the average amount raised per ICO being approximately $11.52 million.<a href ="https://blog.upay.best/initial-coin-offeringico-statistics/">(source)</a> In addition to gaining capital, an ICO is a way to gain insight at a stage where there’s still a lot of uncertainty around what the value of a digital platform will be.<a href="https://mitsloan.mit.edu/ideas-made-to-matter/pros-and-cons-icos-entrepreneurs">(source)</a> A Boston College study recently analyzed ICO data and found an average investor earns returns of 179% from the ICO price to the first day’s opening market price.<a href="https://www.investopedia.com/news/average-investor-earns-179-ico-pop-first-day-trading-study/">(source)</a></p>
   
    <p><b><u>Definition of Capital Type</b></u><br>
    1) An initial coin offering (ICO) is the cryptocurrency industry’s equivalent to an initial public offering (IPO). A company looking to raise money to create a new coin, app, or service launches an ICO as a way to raise funds. Interested investors can buy into the offering and receive a new cryptocurrency token issued by the company. This token may have some utility in using the product or service the company is offering, or it may just represent a stake in the company or project. ICO’s are a popular fundraising method used primarily by startups wishing to offer products and services, usually related to the cryptocurrency and blockchain space. (Smith, 2021)</p>
                             
    <p>2) In many cases, ICOs are security offerings and need to be registered. However, they may not need to register under certain circumstances. Rule 504 of Regulation D does allow companies to offer and sell up to $10 million in securities in a 12-month period if they have filed Form D after first selling their securities. Coin issuers who sell coins to investors as securities can do so legally if they comply with this rule. You can check the SEC's EDGAR database to see if a company has filed its form. (Team, 2024)</p>
                             
    <p>3) When a cryptocurrency project aims to gather resources through an ICO, the first step is to determine the structure of the coin. ICOs can be structured in several ways. For instance, a company can set a specific resource goal or limit, meaning each token distributed in the ICO has a preset price, and the total token supply is static. Alternatively, an ICO can have a static supply of tokens and a dynamic resource goal, meaning the amount of resources received in the ICO determines the overall price per token. Some ICOs have a dynamic token supply but a static price, meaning the amount of resources received determines the final token supply.</p>
                             
    <p>ICOs differ from traditional fundraising methods in several ways. Unlike venture capital or crowdfunding platforms, ICOs can gather resources directly from anyone with a crypto-wallet, anywhere in the world. This method of gathering resources is direct, provides liquidity, and requires minimal bureaucracy. However, it's important to note that while ICOs can provide a funding mechanism and an innovative approach for startups to gather resources, they also carry risks. Due to the lack of regulation and enforcement of securities law, ICOs have been the vehicle for scams and fraud. Therefore, participants must exercise a high degree of caution and diligence when researching and participating in them.</p>
    
    <p>ICOs may provide several benefits, including directness, liquidity, and the absence of gatekeepers. They can attract early adopters and align the early user base behind the success of the project. However, they also come with significant disadvantages. ICOs are, for the most part, completely unregulated, which means participants must exercise a high degree of caution. Numerous ICOs have turned out to be fraudulent or have performed poorly, and fewer than half of all ICOs survive four months after the offering. (What are Initial Coin Offerings (ICOs) and how do they work?, n.d.)</p>    
                          
    <p>4) To protect your investment: Ensure the ICO is legal, research the ICO, analyze the whitepaper, become familiar with the team, learn the business case and learn the Tokenomics. ICOs remain a profitable investment given the right circumstances. As with any investment, it's essential that you study the ICO and its team members. Familiarize yourself with the research done beforehand, analyze the white paper, and become familiar with its target market, regulatory environment, and any likely competitors. By taking those actions upfront, you can more easily spot suspicious projects or hone in on solid investments. (Reiff, 2024)
    </p>
                               
    <u><b><p>References</u></b><br>
    Reiff, N. (2024, July 28). How to Reap Profits on an ICO. Retrieved from Investopedia: <a href="https://www.investopedia.com/tech/what-makes-successful-ico">https://www.investopedia.com/tech/what-makes-successful-ico/</a></p>
                             
    <p>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.</p>
                             
    <p>Team, T. I. (2024, June 2). Initial Coin Offering (ICO): Coin Launch Defined, With Examples. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/i/initial-coin-offering-ico.asp">https://www.investopedia.com/terms/i/initial-coin-offering-ico.asp</a></p>
                             
    <p>What are Initial Coin Offerings (ICOs) and how do they work? (n.d.). Retrieved from Coinbase: <a href="https://www.coinbase.com/learn/tips-and-tutorials/what-are-initial-coin-offerings-and-how-do-they-work">https://www.coinbase.com/learn/tips-and-tutorials/what-are-initial-coin-offerings-and-how-do-they-work</a></p>                                                  

    
                                                                                                            
    <p><u><b>Legal Qualification Requirements</u></b>
    <br>1. Determine the Nature of the Token - Tokens are classified as either utility tokens or security tokens, and this distinction influences the legal framework under which the ICO falls.
    <br>Utility Tokens provide access to a product or service within the platform but are not designed to be an investment. They are generally subject to less regulation.
    <br>Security Tokens are financial instruments, and their issuance is regulated by securities laws. If the token is considered a security, the business must comply with the laws governing the sale of securities, such as those of the U.S. Securities and Exchange Commission (SEC).

    <p>2. Compliance with Securities Laws - The SEC classifies tokens as securities if they meet the criteria of the Howey Test, which looks at whether the token represents an investment of money in a common enterprise with the expectation of profits primarily from the efforts of others. If tokens are deemed securities, the company must register the ICO with the SEC or seek an exemption (e.g., Regulation D or Regulation S exemptions).</p>
                             
    <p>3. Know Your Customer (KYC) and Anti-Money Laundering (AML) Compliance
    <br>KYC Procedures: Companies must implement KYC procedures to verify the identity of potential investors, particularly to prevent fraud, money laundering, and the financing of terrorism. This includes collecting and verifying personal identification information.
    <br>AML Requirements: ICOs are required to adhere to Anti-Money Laundering laws that help prevent illicit financial activities. This includes monitoring and reporting suspicious activities to relevant authorities.</p>

    <p>4. Registration or Exemption
    <br>Depending on whether the token is a utility or security, the business must decide whether to register the ICO with relevant financial authorities or seek an exemption.
    <br>SEC Registration: If the token is a security, the business may be required to file a registration statement (e.g., Form S-1 in the U.S.).
    <br>Regulation D or Regulation S Exemption: U.S. companies may use these exemptions for private offerings, but they are subject to specific investor requirements (e.g., accredited investors) and geographic limitations.</p>

    <p>5. Disclosure and Transparency
    <br>Whitepaper Requirements: The company must prepare a detailed whitepaper outlining the project, the purpose of the token, how the funds raised will be used, the risks involved, and the rights and obligations of token holders. 
    <br>Risk Disclosures: Businesses must disclose potential risks to investors, such as regulatory risks, project viability, and technical risks
    <br>Audit and Financial Transparency: For ICOs involving large amounts of capital, businesses may need to have their financials audited and provide information on how raised funds will be allocated.</p> 

    <p>6. Consumer Protection Laws
    <br>Fraud Prevention: ICOs must ensure that they do not mislead potential investors by providing false or misleading information.
    <br>Consumer Rights: Some jurisdictions require that businesses respect consumer protection laws, such as the right of withdrawal or the right to refunds in certain cases.</p>

    <p>7. Data Protection and Privacy Laws
    <br>Local Data Protection Laws: Compliance with local privacy laws in different jurisdictions where investors reside may also be required.</p>

    <p>8. Cross-Border Considerations
    <br>International Laws: ICOs often attract investors from multiple countries. A business must comply with international regulations, including restrictions on advertising or offering the ICO to residents of certain jurisdictions (e.g., China has banned ICOs and cryptocurrency trading).
    <br>Global Sanctions: ICOs must ensure they are not engaging with individuals or entities on international sanctions lists (e.g., U.S. Office of Foreign Assets Control (OFAC) list, EU sanctions).</p>

    <p>9. Tax Considerations
    <br>Tax Reporting: ICOs often involve the transfer of tokens for money, and businesses must ensure that they are complying with tax reporting requirements. Tax authorities may classify tokens as taxable events, requiring businesses to report gains or losses from the ICO.
    <br>Sales Tax/VAT: Depending on jurisdiction, the sale of tokens may be subject to sales tax or value-added tax (VAT).</p>

    <p>10. Intellectual Property (IP) Protection
    <br>Trademarks and Patents: The company must ensure that it owns or has licenses for any intellectual property used in connection with the ICO (e.g., branding, technology).</p> 

    <p>11. Legal Structure and Governance
    <br>Corporate Structure: The business should be properly structured, and the legal entity should be clear, whether it's a corporation, a limited liability company (LLC), or another type of entity. This helps determine liability, taxation, and legal responsibilities.
    <br>Token Governance: Some projects may include governance tokens, which allow holders to participate in decision-making processes. The legal aspects of token governance must be carefully outlined in the whitepaper and in legal agreements.</p>

    <p>12. Investment Limitation and Cap
    <br>Maximum Raise Limits: Some jurisdictions may set limits on the amount that can be raised in an ICO. 
    <br>Investor Restrictions: Many jurisdictions have restrictions on who can invest in ICOs (e.g., accredited investors, professional investors).</p> 

    <p>13. Ongoing Reporting and Compliance
    <br>Ongoing Filings: In some jurisdictions, businesses must continue filing reports after the ICO, especially if the tokens are considered securities. This may involve providing periodic updates on the status of the project, financial statements, or any material changes to the business.
    <br>Post-ICO Audits: Companies may be subject to audits to verify that the funds raised during the ICO were used as promised.</p>
                                 
    <p><b><u>Supporting Document List</u></b>
    <br>While there is no single, universal form that businesses must submit to initiate an ICO, the SEC requires:
    <br>Form D: For private offerings that may be exempt from full SEC registration.
    <br>AML/KYC Compliance Forms: These forms vary by jurisdiction and may be mandated by financial regulatory bodies.</p>

    <p>Whitepaper: outlines the details of the ICO project. It should explain the business model, the problem the project aims to solve, the technology behind it, tokenomics, roadmap, and team members. Investors rely on the whitepaper to understand the project’s objectives, potential for growth, and the risks involved.</p>

    <p>Tokenomics and Token Sale Structure: A detailed breakdown which includes the number of tokens being offered, the price per token, the distribution plan, and the intended use of the raised capital.</p>

    <p>Legal Documentation: ICOs must comply with local and international laws, including securities regulations, money laundering, and anti-terrorist financing regulations.
    <br>Key Documents:
        <br>• Legal Opinion: A letter or opinion from legal counsel clarifying whether the ICO is a security and subject to regulation under relevant securities laws (this is often required in the U.S. and other jurisdictions with strong securities regulations).
        <br>• Terms and Conditions: A comprehensive agreement that outlines the terms under which investors can participate in the ICO, as well as the rights and obligations of the company and investors.
        <br>• Privacy Policy: A document outlining how the personal data of participants will be handled and protected, in line with data protection laws (e.g., GDPR in the EU).
        <br>• Anti-Money Laundering (AML) and Know Your Customer (KYC) Procedures: Businesses must have a process in place to verify the identity of investors, especially for larger sales or sales involving jurisdictions with stricter regulations.
        <br>• Risk Disclosure Statement: A formal disclaimer detailing the risks associated with the ICO, including regulatory, market, and technological risks.</p>

    <p>Business and Financial Documentation - Supporting business and financial documents that demonstrate the company’s legitimacy and the viability of its project.
    Documents Include: Company Registration Documents, Financial Statements (if applicable), Use of Proceeds and Projected Financial Statements.</p>

    <p>Technology and Security Audits
    <br>Since ICOs are typically linked to blockchain projects, it’s important to demonstrate the security and technical viability of the project.
    <br>Documents Include:
    <br>Smart Contract Audit Report: A report from an independent third-party auditor that verifies the security and functionality of the smart contracts used to issue the tokens.
    <br>Penetration Testing Report: An audit to ensure the platform (website, wallet, etc.) and blockchain infrastructure are secure.
    <br>Code Repository Access: Access to the project’s open-source code (if applicable), especially in cases where transparency is a key factor in building trust with investors.</p>

    <p>Marketing and Promotion Materials that are designed to inform and attract potential investors.
    <br>Documents Include:
    <br>ICO Website and Whitepaper Download: A professional website providing detailed information about the ICO and the ability for investors to download the whitepaper.
    <br>Press Releases and Media Kits: Documents used to publicize the ICO, including news articles, blog posts, social media presence and promotional videos.</p>

    <p>Investor Documentation for KYC/AML Compliance. Documents Include:
        <br>• Identity Verification Forms: Documents to verify the identity of each investor
        <br>• Proof of Address: Recent utility bills or bank statements.
        <br>• Investor Risk Profiling: Assessments of the investor's understanding of the risks involved.</p>

    <p>Jurisdiction-Specific Filings - Depending on where the ICO is being launched, additional filings or permissions may be required such as:
        <br>• Securities Filings: If the ICO is considered a security, it may need to be registered with the relevant securities regulators (e.g., the SEC in the U.S.).
        <br>• Financial Services Licenses: Some jurisdictions may require an ICO to obtain a financial services license or authorization before proceeding with the sale.</p>""")



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def cryptocurrencyinitialcoinofferingfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Cryptocurrency<br>
    Capital Type: Initial Coin Offering</center></p>                        
    <p><center><u><b>Frequently Asked Question for Commercial Initial Coin Offering</u></b></center></p>
                             
    <p><u><b>1. What is an Initial Coin Offering (ICO)?</u></b><br>
    •Answer: An Initial Coin Offering (ICO) is a fundraising method where a company creates and sells a new cryptocurrency or token to the public in exchange for capital. Investors typically purchase these tokens using existing cryptocurrencies like Ethereum or Bitcoin, with the expectation that the tokens will gain value or provide access to a product or service in the future.</p>
                             
    <p><u><b>2. How does an ICO work?</u></b><br>
    • Answer: In an ICO, a company issues a new cryptocurrency or token and offers it to the public. Investors send funds, typically in the form of cryptocurrencies, to the ICO’s wallet in exchange for the newly issued tokens. The company then uses the raised funds to develop its business or project, while investors may use their tokens to access the company’s platform or services once the project is live.</p>
                             
    <p><u><b>3. What are the main advantages of an ICO over traditional fundraising methods?</u></b><br>
    • Answer: ICOs offer several significant advantages. First, they provide global reach, allowing companies to raise capital from investors worldwide. Second, ICOs eliminate the need for traditional intermediaries like banks or venture capitalists, which reduces costs and accelerates the process. Additionally, tokens issued in an ICO can offer utility within a company’s ecosystem, providing value beyond just financial investment. Lastly, ICO tokens are often liquid, meaning they can be traded on exchanges, offering potential liquidity to investors after the ICO concludes.</p>                             
                             
    <p><u><b>4. How much capital can a company raise through an ICO?</u></b><br>
    • Answer: The amount of capital raised in an ICO can vary greatly depending on the project’s size, scope, and market interest. Some ICOs have raised millions of dollars, with large-scale projects reaching $50 million to $100 million or more. Smaller projects may raise anywhere from a few hundred thousand to several million dollars, depending on demand and the strength of the offering.</p>
                             
    <p><u><b>5. What are the key risks involved in conducting an ICO?</u></b><br>
    • Answer: ICOs come with several risks. Regulatory uncertainty is one of the biggest challenges, as ICOs must comply with a variety of local and international regulations. Security risks also exist, as smart contracts, wallets, and exchanges may be vulnerable to hacking. Furthermore, ICO tokens are highly speculative, meaning their value can fluctuate significantly. Finally, there is the reputation risk if the company fails to deliver on its promises or if the ICO is perceived as fraudulent.</p>
                             
    <p><u><b>6. What regulatory considerations should a company be aware of when launching an ICO?</u></b><br>
    • Answer: Companies launching an ICO must comply with various legal and regulatory requirements. Depending on the country, the ICO tokens may be classified as securities, requiring registration or specific disclosures with authorities. Additionally, many ICOs implement Know Your Customer (KYC) and Anti-Money Laundering (AML) procedures to verify the identities of investors and prevent illegal activities. There may also be taxation implications, both for the company and its investors.</p>
                             
    <p><u><b>7. How do I determine if an ICO is the right fundraising method for my business?</u></b><br>
    • Answer: An ICO might be suitable for your business if you have a blockchain-based product or service that can benefit from the issuance of a token. If you're looking to tap into a global investor base without relying on traditional venture capital, an ICO could be a good option. Additionally, if your product or platform can offer token utility, where investors or users can access features through the token, this increases the value proposition. It’s also important to have the resources to navigate legal, technical, and marketing challenges associated with ICOs.</p>
                             
    <p><u><b>8. What are the costs involved in launching an ICO?</u></b><br>
    • Answer: Launching an ICO involves several significant costs, including legal fees for compliance and drafting necessary documents like the whitepaper, terms of service, and privacy policy. Development costs are also substantial, covering the creation of the smart contract, blockchain development, and technical audits. Marketing is another key expense, as building a community and running campaigns to attract investors is crucial to a successful ICO. Additionally, there may be exchange listing fees to get the token listed on cryptocurrency exchanges.</p>
                             
    <p><u><b>9. How long does it take to launch an ICO?</u></b><br>
    • Answer: The process of launching an ICO typically takes between 3 to 6 months, depending on the project’s complexity. This timeline includes market research, legal compliance, smart contract development, community building, and marketing campaigns. The timeline can vary based on the size and scope of the project, as well as the team’s preparedness.</p>
                             
    <p><u><b>10. How do I create a whitepaper for my ICO?</u></b><br>
    • Answer: A whitepaper is a crucial document that outlines your ICO’s goals, the technology behind the project, and the structure of the token (referred to as tokenomics). It should explain the problem your business solves, how the ICO fits into your business model, and what investors can expect in terms of rewards or utility from the token. The whitepaper should be clear, detailed, and professional to build credibility with potential investors.</p>
                             
    <p><u><b>11. How do I ensure the security of my ICO?</u></b><br>
    • Answer: Ensuring security in an ICO involves several key actions. First, have your smart contracts audited by professional cybersecurity firms to identify any vulnerabilities. It’s also essential to implement robust security measures on your platform to protect against hacking, as well as secure wallet systems for storing funds. Additionally, many ICOs require KYC and AML procedures to verify the identities of investors and ensure the integrity of the fundraising process.</p>
                             
    <p><u><b>12. What happens after the ICO ends?</u></b><br>
    • Answer: After the ICO concludes, the company will typically begin distributing tokens to investors. The company then uses the raised funds to develop the product or platform as outlined in the whitepaper. If the token is meant to be traded, the company may work on getting the token listed on exchanges for public trading. The company also continues with product development and community engagement to maintain interest and confidence in the project.</p>
    
    <p><u><b>13. How do I market my ICO effectively?</u></b><br>
    • Answer: Marketing an ICO involves building a strong online presence and engaging with the crypto community. Use social media platforms, forums, and chat channels like Telegram and Discord to create buzz. Partner with influencers in the crypto space and leverage press releases to generate media attention. It’s also important to provide clear communication about the ICO’s value proposition and to ensure that your team is visible and active in addressing potential investors' questions.</p>
                                                      
    <p><u><b>14. What happens if my ICO is not successful?</u></b><br>
    • Answer: If your ICO fails to reach its fundraising goal, the company may return the funds to investors (in cases where a soft cap was set). Alternatively, you could relaunch the ICO after adjusting the offering or improving the product. In some cases, if the ICO fails to meet expectations, the company may pivot its business model or change its fundraising strategy, possibly by seeking venture capital or other financing options.</p> 
                             
    <p><u><b>15. How can I build trust with potential ICO investors?</u></b><br>
    • Answer: Trust can be established through transparency by regularly communicating updates, progress reports, and detailed plans for the project. Additionally, ensuring strong security measures, including third-party audits and secure platforms, helps build investor confidence. Highlighting the credibility of your team and advisors, as well as complying with legal regulations, can further reassure investors of your legitimacy and commitment to the success of the project.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def cryptocurrencyinitialcoinofferingtwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Initial Coin Offering</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage of development for a company seeking to use a cryptocurrency Initial Coin Offering (ICO) generally falls into the early to growth stages of a business’s lifecycle.
    <br>The ideal stage for a company launching an ICO is typically:
        <br>• Early or Growth Stage (but after development of an MVP).
        <br>• Product or service is in development, with a working prototype or demo.
        <br>• Well-defined vision, whitepaper, and tokenomics.
        <br>• A company should have a pre-existing community and market validation to support the ICO.
        <br>• A strong, capable team in place, with legal and regulatory compliance considered.
        <br>• A clear, scalable business model and a well-structured plan for token utility.
    <br>At this stage, the company can use the funds raised from the ICO to accelerate product development, expand the user base, and build out the infrastructure necessary to bring the vision to life.</p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    <br>The ideal entity type for a business looking to use a cryptocurrency Initial Coin Offering (ICO) depends on several factors such as the jurisdiction, the company's goals, and the type of business. However, some entity types are generally better suited for ICOs due to regulatory, legal, and operational considerations.
    <br>For businesses planning to raise significant funds and scale, a C-Corporation is often the best choice, especially for U.S.-based companies. If the goal is to create a decentralized platform, a foundation might be preferable. For global fundraising with fewer regulations, an offshore entity could be ideal.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Raising pre-capital before an ICO is not only acceptable but often essential for companies in the cryptocurrency and blockchain space. It allows businesses to develop the project, validate the concept, build a community, and meet legal and regulatory requirements. However, it is important to maintain transparency about the sources and structure of this early capital, and to ensure that pre-sale investments align with the tokenomics and pricing strategy for the public ICO. 
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Raising pre-capital before launching a cryptocurrency ICO is common and often necessary, but it can create several potential challenges, including:
        <br>• Regulatory issues (compliance with securities laws and regulations).
        <br>• Lock-up periods or vesting schedules that may create issues with token distribution.
        <br>• Tokenomics conflicts, such as discrepancies in token pricing, allocation, and dilution.
        <br>• Valuation discrepancies that could cause friction between pre-capital investors and ICO participants.
        <br>• Legal and contractual restrictions, including pre-sale agreements and investor rights.
        <br>• Market manipulation risks, particularly from large pre-capital investors holding substantial token supply.
    <br>To ensure the ICO proceeds smoothly, businesses should ensure that all pre-capital raises are properly structured, compliant with regulations, and transparent to avoid conflicts and mitigate risks related to fairness, legal challenges, and market volatility. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    There is no limit to how much money a company can raise using IPOs. While the largest ICOs have raised billions (e.g., EOS at $4.1 billion), most ICOs raise between $10 million and $50 million. ICOs are still subject to market dynamics, and companies must ensure they are compliant with regulatory frameworks to successfully raise capital and avoid legal pitfalls.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company launching an ICO is typically the Series A stage or a pre-ICO round. At this point, the company is sufficiently developed to launch an ICO, having validated the project’s concept, created an MVP, and built a community around the project. The Series A round allows the company to raise larger sums for continued development, market expansion, and scaling. Pre-ICO sales can also help generate initial capital and build momentum before the public launch. However, companies can technically conduct an ICO at any stage, from seed to Series B, depending on their needs, market readiness, and product maturity.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Yes, you can use more than one tranche to raise capital via a cryptocurrency Initial Coin Offering (ICO). Many projects adopt this approach to manage fundraising effectively, optimize token distribution, and incentivize different groups of investors. Each tranche may have varying pricing, token allocation, and terms, and can help build momentum, create market demand, and avoid oversubscription. However, careful planning is necessary to ensure that the tranches are structured in a way that maximizes both capital raised and investor confidence while maintaining regulatory compliance.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    There are no limits on how funds from ICOs are used. Ultimately, the use of ICO funds should align with the business’s overall strategy, ensuring that the capital is allocated effectively to drive product development, market adoption, and long-term sustainability.</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    To successfully launch and execute a cryptocurrency Initial Coin Offering (ICO), a business needs to have a high risk tolerance. ICOs come with substantial risks across a wide range of areas, including market volatility, regulatory uncertainties, security threats, project development challenges, and investor behavior. The company must be comfortable with the possibility of fundraising challenges, market fluctuations, and the inherent uncertainty that comes with this form of capital raising. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    For a business considering launching a cryptocurrency ICO, it is essential to have a high level of capital cost tolerance. ICOs are capital-intensive ventures that involve significant upfront investment in legal compliance, development, security, marketing, and operations. Businesses should be prepared for expenses in the range of hundreds of thousands to millions of dollars, depending on the scope and scale of the ICO.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The total cost to launch an ICO can range significantly depending on the project’s size, scope, and complexity. For an average ICO of medium scale, businesses can expect to spend between $300,000 to $2 million in upfront costs. For larger, more complex ICOs, especially those targeting major exchanges and requiring extensive legal and marketing efforts, the costs could reach as high as $5 million or more.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The timeline for launching a cryptocurrency Initial Coin Offering (ICO) can vary significantly based on factors such as project complexity, legal requirements, and the team’s preparation. However, a typical ICO launch process can take anywhere from 3 to 6 months, with some more streamlined projects potentially launching in as little as 2-3 months. In general, most companies can start accessing funds shortly after the ICO concludes, but any escrow, regulatory requirements, or exchange listings can affect the exact timeline.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)