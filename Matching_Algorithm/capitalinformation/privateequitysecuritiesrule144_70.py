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


def privateequitysecuritiesrule144_(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Rule 144</center></p>
    
    <p><b><u>Introduction</u></b><br>
    From November 2023 to April 2024, $85 million dollars was raised using Rule 144, with some of the top filing exceeding $900 million <a href="https://washingtonservice.com/blog/april-2024-144-market-report/">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) Restricted securities are securities acquired in unregistered, private sales from the issuing company or from an affiliate of the issuer. Investors typically receive restricted securities through private placement offerings, Regulation D offerings, employee stock benefit plans, as compensation for professional services, or in exchange for providing "seed money" or start-up capital to the company. Rule 144(a)(3) identifies what sales produce restricted securities.

    <br><br>Control securities are those held by an affiliate of the issuing company. An affiliate is a person, such as an executive officer, a director or large shareholder, in a relationship of control with the issuer. Control means the power to direct the management and policies of the company in question, whether through the ownership of voting securities, by contract, or otherwise. If you buy securities from a controlling person or "affiliate," you take restricted securities, even if they were not restricted in the affiliate's hands.

    <br><br>If you acquire restrictive securities, you almost always will receive a certificate stamped with a "restrictive" legend. The legend indicates that the securities may not be resold in the marketplace unless they are registered with the SEC or are exempt from the registration requirements. Certificates for control securities usually are not stamped with a legend.

    <br><br>What Are the Conditions of Rule 144?
    <br>If you want to sell your restricted or control securities to the public, you can meet the applicable conditions set forth in Rule 144. The rule is not the exclusive means for selling restricted or control securities, but provides a "safe harbor" exemption to sellers. The rule's five conditions are summarized below:

    <br><br>Additional securities purchased from the issuer do not affect the holding period of previously purchased securities of the same class. If you purchased restricted securities from another non-affiliate, you can tack on that non-affiliate's holding period to your holding period. For gifts made by an affiliate, the holding period begins when the affiliate acquired the securities and not on the date of the gift. In the case of a stock option, including employee stock options, the holding period begins on the date the option is exercised and not the date it is granted.

    <br><br>• Holding Period. Before you may sell any restricted securities in the marketplace, you must hold them for a certain period of time. If the company that issued the securities is a “reporting company” in that it is subject to the reporting requirements of the Securities Exchange Act of 1934, then you must hold the securities for at least six months. If the issuer of the securities is not subject to the reporting requirements, then you must hold the securities for at least one year. The relevant holding period begins when the securities were bought and fully paid for. The holding period only applies to restricted securities. Because securities acquired in the public market are not restricted, there is no holding period for an affiliate who purchases securities of the issuer in the marketplace. But the resale of an affiliate's shares as control securities is subject to the other conditions of the rule.

    <br><br>• Current Public Information.  There must be adequate current information about the issuing company publicly available before the sale can be made. For reporting companies, this generally means that the companies have complied with the periodic reporting requirements of the Securities Exchange Act of 1934. For non-reporting companies, this means that certain company information, including information regarding the nature of its business, the identity of its officers and directors, and its financial statements, is publicly available.

    <br><br>• Trading Volume Formula. If you are an affiliate, the number of equity securities you may sell during any three-month period cannot exceed the greater of 1% of the outstanding shares of the same class being sold, or if the class is listed on a stock exchange, the greater of 1% or the average reported weekly trading volume during the four weeks preceding the filing of a notice of sale on Form 144.  Over-the-counter stocks, including those quoted on the OTC Bulletin Board and the Pink Sheets, can only be sold using the 1% measurement.

    <br><br>• Ordinary Brokerage Transactions.  If you are an affiliate, the sales must be handled in all respects as routine trading transactions, and brokers may not receive more than a normal commission. Neither the seller nor the broker can solicit orders to buy the securities.

    <br><br>• Filing a Notice of Proposed Sale With the SEC.  If you are an affiliate, you must file a notice with the SEC on Form 144 if the sale involves more than 5,000 shares or the aggregate dollar amount is greater than $50,000 in any three-month period. (Rule 144: Selling Restricted and Control Securities, 2013)

    <br><br>2) An important hurdle to qualifying for this exemption is complying with the Rule 144 holding period for each issuance before the resale of the security. If the issuing company is a reporting company with regards to the Securities Exchange Act of 1934, the qualifying holding period is six months. If the company is not a reporting company, the qualifying holding period is one year. The Rule 144 holding period begins from the security’s original date of issuance regardless of resale or conversion. (Diefendorf, 2017)  

    <br><br>3) SEC Rule 144 applies to unregistered securities based on cryptocurrencies or blockchain-based tokens.

    <br><br>While tokens like Bitcoin are not currently classified as securities and would not be subject to Rule 144, financial products that offer interest, yield, or dividends based on lending or "staking" such crypto tokens may fall under the definition of securities.

    <br><br>The SEC is reportedly investigating several crypto exchanges including Kraken, Gemini, and Genesis, following the spectacular collapse of FTX. In particular, the SEC is looking into whether these and other exchanges broke the rules by illegally offering unregistered securities to U.S. customers.

    <br><br>Are Cryptocurrencies Securities?
    <br>If a security is determined to be a restricted security as defined by SEC Rule 144, it can only be resold under specific circumstances, including the passage of time, the filing of Form 144, and compliance with the quantity limitations imposed by the rule.

    <br><br>Crypto exchanges Genesis and Gemini were sued by the SEC in January of 2023 for the unregistered offer and sale of securities to customers through an interest-bearing product. This highlights the increased scrutiny that the crypto industry is facing from regulators such as the SEC, which has been taking enforcement action against crypto companies that violate rules and has called for them to get into compliance with existing regulations. (Hayes, 2023) 
    </p>
                             
    <u><b><p>References</u></b><br>
    Diefendorf, K. (2017, December 18). Rule 144. Retrieved from Carta: <a href="https://carta.com/learn/startups/equity-management/rule-144/">https://carta.com/learn/startups/equity-management/rule-144/
    <br>Hayes, A. (2023, February 19). SEC Rule 144: Definition, Holding Periods, and Other Rules. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/r/rule144">https://www.investopedia.com/terms/r/rule144</a>
    <br>Rule 144: Selling Restricted and Control Securities. (2013, January 15). Retrieved from SEC: <a href="https://www.sec.gov/about/reports-publications/investorpubsrule144">https://www.sec.gov/about/reports-publications/investorpubsrule144</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>Public Reporting Status:
        <br>• The company must be a publicly traded company that files regular reports with the SEC (such as Form 10-K, Form 10-Q, Form 8-K).
        <br>• The company must be up-to-date with its filing obligations (i.e., it must not be delinquent in SEC filings).

    <br><br>Holding Period:
        <br>• Non-affiliate holders: Securities must be held for at least 6 months before they can be sold under Rule 144.
        <br>• Affiliate holders: Securities must be held for at least 12 months before they can be sold under Rule 144.
    <br>The holding period begins when the securities were originally issued, not when they areresold.

    <br><br>Adequate Public Information:
        <br>• The company must provide current, public information about its financial condition and operations. This typically includes having up-to-date financial statements that meet the SEC’s disclosure requirements.
        <br>• If the company has been public for less than 90 days, the information provided must meet the SEC’s current public information standard.

    <br><br>Volume Limitations:
    <br>For affiliate transactions (e.g., insiders or significant shareholders), the amount of securities that can be sold in any 3-month period is limited to:
        <br>• The greater of 1% of the company’s outstanding shares, or
        <br>• The average weekly trading volume of the company's shares during the 4-week period preceding the sale.
    
    <br><br>Manner of Sale:
        <br>• The securities must be sold in a broker’s transaction or directly with a market maker.
        <br>• The sale cannot be directly from the company’s treasury (e.g., the company cannot engage in an underwritten offering under Rule 144).

    <br><br>Filing Form 144:
        <br>• Affiliate sellers must file Form 144 with the SEC if the amount of securities being sold exceeds 5,000 shares or $50,000 in any 3-month period.
        <br>• Form 144 provides notice of the proposed resale and must be filed at the time of sale.
        <br>• No Integration with Other Offerings:

    <br><br>The sale of securities under Rule 144 must not be part of an integrated offering with other public or private securities offerings. This means the resale of restricted securities must be treated independently from other capital-raising efforts.

    <br><br>No "Shell" Status:
    <br> The company must not be a "shell company". A shell company is one that has no significant operations or assets. The company must have active business operations to be eligible to use Rule 144.
    <br> No Disqualifying Events:
    <br> The company must not have experienced any disqualifying events that would prevent the resale of securities under Rule 144. These could include certain legal or regulatory violations.

    <br>Evergreen Rule:
    <br>Although not a formal legal requirement, the evergreen rule means that the holding period for restricted securities can be transferred when the securities are sold or transferred from one holder to another, under certain conditions. The new holder can continue using the original holding period without having to wait for a new holding period to be established.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>Current SEC Filings and Financial Reports including:
    <br>- Form 10-K (Annual Report
    <br>- Form 10-Q (Quarterly Reports
    <br>- Form 8-K (Current Reports)
    <br>- Form 20-F or 40-F (for foreign companies)

    <br><br>Holding Period Documentation:
    <br>- Proof of Original Acquisition Date
    <br>- Transfer Records

    <br><br>Form 144 (For Affiliate Sales):
    <br>- Form 144 Filing
    <br>- Details of the Proposed Sale
    <br>- Signature of the Selling Shareholder

    <br><br>Company’s Public Information:
    <br>- Financial Statements
    <br>- Investor Disclosures
    <br>- Legal Opinion (if applicable)

    <br><br>No Shell Company Status:
    <br> -Verification of Business Operations including:
    <br> -Documentation of ongoing business operations, revenue generation, or assets.
    <br> -Confirmation of recent activity (e.g., filings, product sales, ongoing business agreements).

    <br><br>Volume Limit Documentation (For Affiliates):
    <br>Shareholder Agreement or Shareholding Information
    <br>Trading Data

    <br><br>Compliance with Reporting Obligations:
    <br>Securities Registration Status
    <br>Independent Auditor’s Report

    <br><br>Legal and Regulatory Compliance Documentation:
    <br>Legal Opinion (if necessary)
    <br>Disclosures of Disqualifying Events

    <br<br>Manner of Sale:
    <br>Broker’s Transaction Documentation
    <br>Proof of Public Market
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesrule144_faq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Equity Securities<br>
    Capital Type: Rule 144</center></p>                        
    <p><center><u><b>Frequently Asked Question for Rule 144</u></b></center></p>
    <p><u><b>1. What is Rule 144, and how does it relate to raising capital?</u></b><br>
    • Answer: Rule 144 is an SEC regulation that provides a safe harbor for the resale of restricted and control securities. It allows companies and their affiliates to sell privately issued securities into the public markets, under specific conditions. Rule 144 is commonly used by businesses that have issued restricted stock through private placements and want to facilitate the resale of those securities, often as part of a larger strategy to raise capital in secondary offerings.</p>
                             
    <p><u><b>2. Why should my company consider using Rule 144 to raise capital?</u></b><br>
    • Answer: Rule 144 can be an attractive option for companies seeking to unlock liquidity in their restricted securities. It allows businesses to access capital by reselling existing securities, rather than issuing new shares. This can be an appealing alternative for companies that want to avoid additional dilution of ownership or those looking to provide liquidity to early investors, employees, or insiders.</p>
                             
    <p><u><b>3. What types of securities are eligible for resale under Rule 144?</u></b><br>
    • Answer: Rule 144 applies to restricted securities, which are typically securities that were acquired through private placements or offerings not registered with the SEC. It also applies to control securities, which are owned by insiders, affiliates, or large shareholders of the company. These securities can be resold under Rule 144, provided the resale meets the specific holding period, volume, and other requirements.</p>
                             
    <p><u><b>4. What are the key requirements for using Rule 144 to sell restricted securities?</u></b><br>
    • Answer: To resell restricted securities under Rule 144, the company must meet the following requirements:
    <br>- Holding Period: The securities must have been held for at least 6 months by a non-affiliate or 12 months by an affiliate.
    <br>- Current Public Information: The company must be current in its SEC filings, typically requiring at least one year of ongoing public reporting.
    <br>- Volume Limits: Sales by an affiliate are limited to the greater of 1% of outstanding shares or the average weekly trading volume over the last four weeks.
    <br>- Manner of Sale: Securities must be sold in a broker's transaction or through a market maker.
    <br>- Adequate Disclosure: For affiliates, a Form 144 must be filed with the SEC if the amount of securities being sold exceeds 5,000 shares or $50,000.</p>
                             
    <p><u><b>5. How long do I need to hold the securities before I can sell them under Rule 144?</u></b><br>
    • Answer: The holding period is typically 6 months for non-affiliates and 12 months for affiliates. This means that securities must be held by the seller for this period before they are eligible for resale under Rule 144.
    </p>
                             
    <p><u><b>6. Can my company use Rule 144 if it is not publicly traded or does not file with the SEC?</u></b><br>
    • Answer: No. Rule 144 only applies to companies that are public reporting companies, meaning they file regular reports with the SEC (e.g., Form 10-K, 10-Q, or 8-K). If the company is not publicly traded, it will need to be in compliance with SEC reporting requirements before it can use Rule 144 for resale of securities.</p>
                             
    <p><u><b>7. How can Rule 144 help me raise capital without issuing new shares?</u></b><br>
    • Answer: Rule 144 allows companies to sell previously issued, restricted securities (such as shares acquired in private placements) without issuing new stock. This can help raise capital for the company or provide liquidity for early investors and employees without diluting ownership by issuing more shares.</p>
                             
    <p><u><b>8. What are the key advantages of using Rule 144 to raise capital?</u></b><br>
    • Answer: Some of the key advantages of using Rule 144 to raise capital include:
    <br>- Liquidity for Investors: It allows early investors or insiders to liquidate their holdings and provide liquidity, which can make it easier to attract future investment.
    <br>- Avoid Dilution: Since Rule 144 focuses on reselling existing securities rather than issuing new ones, it avoids diluting the ownership of existing shareholders.
    <br>- Flexible Financing Option: Rule 144 can be used as a means for secondary offerings, enabling companies to raise capital through resales without needing to conduct a public offering or new financing round.</p>
                             
    <p><u><b>9. Are there any risks associated with using Rule 144 to raise capital?</u></b><br>
    • Answer: Yes, there are some risks, including:
    <br>- Market Conditions: The price of the company’s shares may be volatile, and large resale transactions under Rule 144 could impact the stock price.
    <br>- Limited Resale Volume: Rule 144 limits the number of securities that can be resold, which may impact the speed and volume of capital raised.
    <br>- Compliance Risks: Failure to meet the conditions of Rule 144, such as reporting requirements or holding period, can result in the securities being ineligible for resale, creating legal and regulatory risks.</p>
                             
    <p><u><b>10. How much capital can my company raise using Rule 144?</u></b><br>
    • Answer: The amount of capital your company can raise through Rule 144 is not directly limited by the rule itself. However, the rule imposes volume limits on sales by affiliates (1% of outstanding shares or the average weekly trading volume). The actual amount that can be raised will depend on the volume of shares eligible for resale, market conditions, and investor interest.</p>
                             
    <p><u><b>11. How quickly can my company raise capital using Rule 144?</u></b><br>
    • Answer: The timeline to raise capital using Rule 144 can vary, but the resale process itself can be completed relatively quickly (in a few weeks) once the securities are eligible for resale. However, the company must meet certain eligibility criteria, such as the holding period, reporting requirements, and other factors, which may delay the process if they are not already met.</p>
                             
    <p><u><b>12. Do I need to hire a financial advisor or placement agent to use Rule 144?</u></b><br>
    • Answer: No, you do not necessarily need to hire a financial advisor or placement agent to resell securities under Rule 144, but many companies choose to do so for guidance on compliance and market strategy. A placement agent may also assist in finding buyers for the securities, especially if large amounts are being resold.
    </p> 
                             
    <p><u><b>13. How does Rule 144 differ from a public offering or other private capital raises?</u></b><br>
    • Answer: The key difference is that Rule 144 focuses on the resale of existing securities, rather than issuing new securities as with public offerings or private placements. While public offerings or private capital raises involve issuing new shares, Rule 144 allows for liquidity in restricted or control securities that have already been issued.</p>

    <p><u><b>14. What if my company has not yet filed required SEC reports—can we still use Rule 144?</u></b><br>
    • Answer: If your company is not yet current with SEC filings, it will need to become current before it can use Rule 144. A company must file at least one year’s worth of SEC reports to be considered a reporting company, making its securities eligible for resale under Rule 144.</p>
    
     <p><u><b>15. Can insiders or affiliates use Rule 144 to sell shares?</u></b><br>
    • Answer: Yes, insiders (such as executives or significant shareholders) can use Rule 144 to sell shares, but they are subject to more stringent requirements than non-affiliates. These include the 12-month holding period, volume limits, and filing a Form 144 if the sale exceeds certain thresholds.</p>
    
     <p><u><b>16. What happens if my company doesn’t comply with Rule 144’s requirements?</u></b><br>
    • Answer: If the company or its shareholders fail to comply with the requirements of Rule 144 (such as the holding period, reporting obligations, or volume limits), the securities may not be eligible for resale under Rule 144, and the company could face legal consequences. Non-compliance could also result in the reputational risk of not adhering to securities laws.</p>                         
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesrule144_twelve(request):
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
    Capital Type: Rule 144</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage of development for a company to use Rule 144 is typically post-revenue or growth stage, where the company has a certain degree of operational stability, is possibly public or has required filings, and has adequate reporting mechanisms in place to ensure compliance with SEC regulations.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    <br>The ideal entity type for using Rule 144 is a C-corporation, as it is the most straightforward structure for facilitating the resale of restricted securities under this rule. C-corporations can issue shares of stock that are easily categorized as securities, making it easier to comply with the SEC's reporting requirements and resale conditions under Rule 144.
    <br>LLCs can also use Rule 144, but they need additional structuring to make their membership interests transferable as securities. S-corporations are typically not suitable due to shareholder limitations, and private equity funds typically utilize Rule 144 for investments in C-corporations rather than for their own direct use.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    It is allowable for a business to have raised capital before using Rule 144 for the resale of private equity securities. The important factors are that the securities raised in private placements are typically restricted, meaning they cannot be resold immediately. The business must ensure that the required holding period (typically six months or one year depending on the company’s reporting status) has passed before investors can sell those securities under Rule 144. Therefore, businesses can raise capital in advance, and once the conditions for Rule 144 are met, they can use the rule to allow liquidity for investors holding those restricted securities.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While a company can raise pre-capital before using Rule 144, there are several restrictions that could interfere with the use of the rule for reselling securities. The most notable issues include:
    <br>- The need for the raised capital to involve restricted securities (e.g., through private placements or exemptions like Regulation D).
    <br>- Compliance with SEC reporting requirements (if applicable).
    <br>- Adherence to conditions for selling restricted securities, including holding periods and affiliate/insider restrictions.
    <br>If the company does not meet the necessary criteria (e.g., issuing non-restricted securities or failing to report), Rule 144 may not be applicable for reselling those securities. Companies must ensure that their capital raises and securities offerings are structured in a way that aligns with Rule 144’s requirements for future resales. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The amount of capital your company can raise through Rule 144 is not directly limited by the rule itself. However, the rule imposes volume limits on sales by affiliates (1% of outstanding shares or the average weekly trading volume). The actual amount that can be raised will depend on the volume of shares eligible for resale, market conditions, and investor interest.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    <br>The ideal capital rounds for a company that wants to use Private Equity Securities Rule 144 are typically those involving private placements under Regulation D (especially Rule 506(b) and 506(c)). These rounds usually issue restricted securities, which are the type of securities that Rule 144 governs for resale. This includes:
    <br>- Seed, Series A, Series B, and other growth stage rounds that issue restricted securities.
    <br>- Pre-IPO rounds, where investors may want to resell their securities once the holding period and other conditions under Rule 144 are met.
    <br>Rule 144 allows for the resale of these restricted securities after the required holding periods (typically 6 months or 1 year) have passed, giving investors potential liquidity while also enabling companies to raise capital privately.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    You can use more than one tranche of securities and still resell them under Rule 144, provided each tranche satisfies the rule's conditions. Each tranche has its own holding period and volume limitations (for affiliates), so the resale of securities from different tranches may happen at different times based on when the holding period for each tranche is met. Non-affiliate investors are generally free to resell once the holding period is over, while affiliate investors are subject to volume limits under Rule 144, which apply separately to each tranche of securities.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A business cannot directly use funds from the resale of securities under Rule 144, as it only benefits from the initial issuance of those securities. However, the company can use the proceeds from private placements or other private offerings (prior to Rule 144 resale) for various business activities like expansion, debt repayment, acquisitions, and R&D. The business can also benefit from Rule 144 indirectly by enhancing its liquidity and market valuation, which can help in securing future rounds of funding.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    When a business considers using Private Equity Securities Rule 144, there are several risks and challenges involved. A business needs to have a moderate to high risk tolerance, as the process of using Rule 144 involves navigating regulatory, financial, and market risks. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The business should have a high risk tolerance for capital costs since navigating the complexities of Rule 144 requires a significant investment in legal, financial, and administrative resources. It also requires a strategic approach to managing the potential impacts on market liquidity, stock price, and future fundraising efforts.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    For an average small to mid-sized company, the upfront costs for using Private Equity Securities Rule 144 typically range from $30,000 to $200,000 depending on factors like the company's size, stage of development, and whether it is already publicly traded. For larger, more complex companies, these costs could rise significantly, particularly in terms of legal, audit, and placement agent fees. If the company is already publicly traded and has some of these systems in place, the upfront costs may be lower.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    A company that is ready and compliant with Rule 144 can expect to access capital in a few weeks to a few months, but the actual speed of resale will be affected by the company’s readiness, the nature of the securities, and the market conditions.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)