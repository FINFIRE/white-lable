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


def privateequitysecuritiesregulationa(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation A+</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Reg A+ is ideal for companies raising equity capital in amounts ranging from $5 Million to $75 Million dollars in a given 12-month period of time.  It is designed so that the issuer may sell privately held companies to the public. {n} fits that definition.  Reg A+ has been a viable tool for enterprises for 7 years.  For example, in In the first half of 2024, over $224 million was raised using Regulation A investments.  In 2023, Reg A offerings that were publicly available on major platforms and through the issuer’s own websites raised $225 million.  The total valuation of all equity Regulation A (Reg A) companies raising in May 2023 was $6.6 billion. On average, each Reg A raise in May 2023 had a valuation of $152.7 million. 
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) A "private equity securities Regulation A" refers to a type of public offering where a private equity firm raises capital by selling securities to the public, allowing them to offer a limited amount of securities to a wider pool of investors than traditional private placements, while still having less stringent requirements compared to a full public registration process; essentially considered a "mini IPO" option for private equity firms. (SEC, 2024)

    <br><br>2) Regulation A is an exemption from registration for public offerings that has two offering tiers: Tier 1, for offerings of up to $20 million in a 12-month period; and Tier 2, for offerings of up to $75 million in a 12-month period. For offerings of up to $20 million, companies can elect to proceed under the requirements for either Tier 1 or Tier 2.

    <br><br>There are certain basic requirements applicable to both Tier 1 and Tier 2 offerings, including company eligibility requirements, bad actor disqualifications provision, disclosure, and other matters. Additional requirements apply to Tier 2 offerings, including limitations on the amount of money a non-accredited investor may invest in a Tier 2 offering, requirements for audited financial statements and the filing of ongoing reports. Issuers in Tier 2 offerings are not required to register or qualify their offerings with state securities regulators. (Carter, 2018)

    <br><br>3) Regulation A+ has been around for years but has not been widely used mainly because of the way the rules were written, making raising capital quite inefficient. In fact, the Securities and Exchange Commission (SEC) estimated only 26 offerings were conducted annually and they were capped at an upper funding limit of $5,000,000. Whereas now, with Regulation A+, companies can raise up to $20,000,000 on Tier 1 and up to $75,000,000 on Tier 2." (Smith, 2021)

    <br><br>4) Under the federal securities laws, any offer or sale of a security must either be registered with the SEC or meet an exemption.  Regulation A is an exemption from the registration requirements, allowing companies to offer and sell their securities without having to register the offering with the SEC. 
    Companies relying on a Regulation A exemption can offer and sell their securities to the public under two different tiers that have two different requirements—Tier 1 and Tier 2.  Under both tiers, the issuer must file an offering statement on Form 1-A with the SEC.  The offering statement includes the offering circular, which is the primary disclosure document for investors.  Investors must be provided with, or given information on how to access, the offering circular.  An issuer can only accept payment for the sale of its securities once its offering statement is qualified by the staff at the SEC.  The SEC’s qualification, however, does not mean that the SEC has approved of the securities offering. The SEC also does not assess the accuracy or completeness of any of the offering documents or solicitation materials.
    Under Tier 1, an issuer can raise up to $20 million in any 12-month period, including no more than $6 million on behalf of selling securityholders that are affiliates of the issuer. In addition to qualification by SEC staff, companies offering securities pursuant to Tier 1 of Regulation A will also need to file and have their offering statements qualified by the state securities regulators in the states in which the issuer plans to sell its securities.  Companies offering securities under Tier 1 do not have ongoing reporting requirements other than a final report on Form 1-Z on the status of the offering.   
    Under Tier 2, an issuer can raise up to $75 million in any 12-month period. Unlike Tier 1 offerings, the offering statement does not have to be qualified by a state securities regulator, and the issuer is subject to ongoing reporting requirements in the form of an annual report on Form 1-K, a semiannual report on Form 1-SA and a current report on Form 1-U.
    Importantly, there are investment limitations for offerings under Tier 2 if the securities offered are not going to be listed on a national securities exchange upon qualification.  Investors either have to be an accredited investor or are limited in how much they can invest to no more than 10% of the greater of the person’s, alone or together with a spouse, annual income or net worth (excluding the value of the person’s primary residence and any loans secured by the residence (up to the value of the residence)). (Regulation A , n.d.)

    <br><br>5) Regulation A+ rules require disclosure documents be filed on EDGAR, allowing the confidential review of offering documents, and permitting certain “testing the waters” communications. (Knight & Hal, 2019) 
    </p>
                             
    <u><b><p>References</u></b><br>
    Carter, D. (2018, October 1). Equity Crowdfunding Requirements – Reg A+. Retrieved from Colonial Stock Transfer: <a href="https://blog.colonialstock.com/equity-crowdfunding-chart-comparison/">https://blog.colonialstock.com/equity-crowdfunding-chart-comparison/</a>

    <br><br>Knight, J. H., & Hal, T. J. (2019). FAQs ABOUT REGULATION A+. Retrieved from Bass Berry Securities Law Exchange : <a href="https://www.bassberrysecuritieslawexchange.com/wp-content/uploads/sites/201/2019/02/Regulation-A-FAQs.pdf">https://www.bassberrysecuritieslawexchange.com/wp-content/uploads/sites/201/2019/02/Regulation-A-FAQs.pdf</a>

    <br><br>Regulation A . (n.d.). Retrieved from Investor: <a href="https://www.investor.gov/introduction-investing/investing-basics/glossary/regulation">https://www.investor.gov/introduction-investing/investing-basics/glossary/regulation</a>

    <br><br>SEC. (2024, November 15). Regulation A. Retrieved from SEC: <a href="https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/regulation">https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/regulation</a>

    <br><br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Be a U.S. or Canadian business entity (corporation, LLC, etc.).
    <br>• Provide audited financial statements for the past two years (or since inception)
    <br>• File Form 1-A with the SEC, including the Offering Circular and financials.
    <br>• Ensure compliance with state securities laws for Tier 1 or benefit from state preemption for Tier 2.
    <br>• Meet disclosure and reporting requirements, including periodic updates for Tier 2 offerings.
    <br>• Decide between a Tier 1 or Tier 2 offering, based on the amount of capital to be raised.
    <br>• Pay filing fees to the SEC and possibly to state regulators (for Tier 1).
    <br>• Use appropriate corporate governance structures to meet SEC and investor requirements.
    <br>• Engage legal and audit counsel to ensure compliance with securities regulations.
    </p>
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Form 1-A (Offering Statement) – The main regulatory filing document.
    <br>• Offering Circular – A comprehensive document providing information about the company and the offering.
    <br>• Audited or Reviewed Financial Statements – Depending on the amount raised.
    <br>• Independent Auditor's Report – If audited financials are provided.
    <br>• Description of Business and Management – Information about the company’s operations and key management.
    <br>• Risk Factors – Disclosures about risks associated with the investment.
    <br>• Use of Proceeds – Details on how the raised funds will be used.
    <br>• State Securities Filings (Tier 1 only) – Compliance with state-level securities regulations.
    <br>• Form 1-Z – A post-offering exit report (Tier 1).
    <br>• Tier 2 issuers must file ongoing reports including "Form 1-K" (annual), "Form 1-SA" (semi-annual), and "Form 1-U" (current event reports) to comply with reporting requirements
    <br>• Marketing Materials – If using general solicitation
    <br>• Additional Documentation – As required by the SEC, such as related-party transaction disclosures or contracts
    <br>• Escrow Agreement (if applicable) – Agreement for holding funds raised.
    <br>• Investor Questionnaire (if applicable) – To verify investor eligibility. 
    </p>
        """)


    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe(introduction.format(n=name))    
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationafaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Equity Securities<br>
    Capital Type: Regulation A</center></p>                        
    <p><center><u><b>Frequently Asked Question for Regulation A</u></b></center></p>
    <p><u><b>1. What is Regulation A+ (Reg A+)?</u></b><br>
    • Answer: Regulation A+ is a set of rules under the Securities Act of 1933 that allows companies to raise capital from both accredited and non-accredited investors. It is often called a "mini-IPO" because it permits companies to offer securities to the public with reduced regulatory requirements compared to a full initial public offering (IPO).</p>
                             
    <p><u><b>2. How much capital can a company raise using Regulation A+?</u></b><br>
    • Answer: A company can raise up to:
    <br>- $20 million in a 12-month period under Tier 1.
    <br>- $75 million in a 12-month period under Tier 2.
    <br>- These limits are set by the SEC and apply to the total amount raised, not just the company’s offering.</p>
                             
    <p><u><b>3. What are the main differences between a Tier 1 and Tier 2 offering under Reg A+?</u></b><br>
    • Answer:
    <br> -Tier 1: Allows the company to raise up to $20 million but requires state-level securities filings in addition to SEC filings. It has less ongoing reporting obligations.
    <br> -Tier 2: Allows companies to raise up to $75 million and provides the benefit of preemption of state securities laws (no need for state-level filings). However, Tier 2 requires ongoing reporting, including annual, semiannual, and current reports to the SEC.</p>
                             
    <p><u><b>4. Who can invest in a Regulation A+ offering?</u></b><br>
    • Answer:     
    <br>- Both accredited and non-accredited investors can invest in Regulation A+ offerings.
    <br>- For Tier 2 offerings, non-accredited investors are limited to investing up to 10% of their annual income or net worth (whichever is greater).
    <br>- This allows companies to access a broader pool of investors compared to private placements, which are typically restricted to accredited investors only.</p>
                             
    <p><u><b>5. What are the benefits of choosing Reg A+ over other fundraising options like venture capital or traditional IPOs?</u></b><br>
    • Answer:     
    <br>- Broader Investor Base: Reg A+ allows companies to raise funds from non-accredited investors, offering access to a larger pool of potential investors.
    <br>- Faster and Less Expensive than an IPO: The process is typically faster and less costly than a traditional IPO. The SEC review process for a Reg A+ offering is generally quicker than an IPO registration.
    <br>- Flexibility in Offering Structure: Companies can structure their offerings more flexibly, allowing for a variety of investment instruments (equity, debt, etc.).
    <br>- No Need for Underwriters: Unlike IPOs, Reg A+ offerings do not require investment banks as underwriters, reducing costs.
    <br>- Ongoing Reporting Requirements (Tier 2): Although ongoing reporting is required for Tier 2 offerings, it can enhance transparency with investors and provide ongoing access to capital markets.
    </p>
                             
    <p><u><b>6. What are the key eligibility requirements to use Reg A+ for raising capital?</u></b><br>
    • Answer:  To be eligible for Reg A+, a company must:
    <br>- Be a U.S. or Canadian business (corporation, LLC, etc.).
    <br>- Have audited financial statements (or reviewed financials, depending on the amount being raised).
    <br>- Provide an offering circular and file Form 1-A with the SEC.
    <br>- Not be a blank check company, investment company, or company with no specific business plan.
    <br>- Be in good standing with the SEC and not under suspension or disqualification.</p>
                             
    <p><u><b>7. What are the costs involved in a Regulation A+ offering?</u></b><br>
    • Answer: The costs of a Reg A+ offering typically include:
    <br> -Legal fees: Costs associated with preparing the offering documents, including Form 1-A and the Offering Circular.
    <br> -Audit fees: If raising more than $20 million (Tier 2), the company must provide audited financials.
    <br> -Filing fees: These are paid to the SEC and possibly state regulators for Tier 1 offerings.
    <br> -Marketing costs: Companies may also incur costs for marketing and promoting the offering, including creating investor presentations or advertisements.
    <br> -Ongoing reporting costs: For Tier 2 offerings, companies will need to budget for the costs of preparing and filing annual and semiannual reports with the SEC.</p>
                             
    <p><u><b>8. What are the disclosure requirements for a Reg A+ offering?</u></b><br>
    • Answer: Companies must disclose:
    <br>- Business description and management information.
    <br>- Financial statements for the past two years (or since inception if the company is less than two years old).
    <br>- Risk factors associated with the business and investment.
    <br>- Use of proceeds from the offering.
    <br>- The terms of the securities being offered, including pricing, rights, and privileges.
    <br>- Governance structure and material contracts.
    <br>- Companies must also provide ongoing disclosures if they conduct a Tier 2 offering.</p>
                             
    <p><u><b>9. What is the SEC review process for a Regulation A+ offering?</u></b><br>
    • Answer: Defaulting on a promissory note can have serious consequences, including:
    <br>- The SEC must qualify the offering before the company can sell securities to investors. The process involves filing Form 1-A, which the SEC will review. The SEC may provide comments and request revisions before granting qualification.
    <br>- The review process typically takes 2 to 3 months, but can vary depending on the complexity of the offering and the responsiveness of the company.
    <br>- Once the SEC qualifies the offering, the company can begin raising capital.</p>
                             
    <p><u><b>10. What are the advantages of Tier 2 over Tier 1?</u></b><br>
    • Answer: Promissory notes are ideal for businesses that:
    <br>- Preemption of State Laws: Tier 2 offerings are not subject to state securities laws (Blue Sky Laws), which can streamline the process and reduce administrative burden compared to Tier 1.
    <br>- Higher Capital Limits: Companies can raise up to $75 million under Tier 2, compared to the $20 million limit for Tier 1.
    <br>- Broader Investor Base: Tier 2 offerings can include both accredited and non-accredited investors, whereas Tier 1 offerings may be subject to state restrictions.
    <br>- Ongoing Reporting: While Tier 2 requires more ongoing reporting (annual, semiannual, and current reports), this increased transparency can improve investor confidence and enhance credibility.</p>
                             
    <p><u><b>11. What are the risks of using Regulation A+ to raise capital?</u></b><br>
    • Answer:
    <br>- Compliance Costs: Preparing for a Reg A+ offering can involve substantial legal and accounting costs, especially for Tier 2 offerings.
    <br>- Ongoing Reporting: Tier 2 offerings require ongoing public reporting, which could expose the company to additional regulatory scrutiny and costs.
    <br>- Investor Perception: Although Reg A+ offers the ability to raise capital from a broad investor base, some investors may view Regulation A+ as less prestigious than an IPO or a private equity raise.
    <br>- Dilution: Issuing equity securities through Reg A+ will dilute existing shareholders, which may be a concern for founders and early investors.</p>
                             
    <p><u><b>12. Can the company use Reg A+ for future fundraising after the initial offering?</u></b><br>
    • Answer: Yes, companies that complete a Regulation A+ offering can conduct additional offerings in the future, subject to the same limits on the amount raised ($20 million for Tier 1, $75 million for Tier 2 per 12-month period). Ongoing access to capital can be a significant advantage of using Reg A+.
    </p> 
                             
    <p><u><b>13. How long does the Regulation A+ process take?</u></b><br>
    • Answer: The process typically takes between 2 to 6 months from filing to SEC qualification, depending on the complexity of the offering, the responsiveness of the company, and the SEC’s review. However, the timeline can vary.</p>

    <p><u><b>14. Can a company raise capital through Reg A+ if it has a limited operating history or early-stage business?</u></b><br>
    • Answer: Yes, Reg A+ can be used by companies at various stages, including early-stage businesses. However, companies with limited operating history must be prepared to provide thorough disclosures about their business model, management team, financial condition, and risks. Audited financial statements will still be required, even for early-stage companies.</p>                         
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationatwelve(request):
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
    Capital Type: Regulation A+</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    While {n} is in the {stage} stage, utilizing Private Equity Securities Regulation A (Reg A+) offers the ability to raise substantial capital (up to $75 million), access a wide investor pool, and gain public exposure.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Utilizing Reg A+ for a C Corporation is a good option. Reg A+ provides valuable benefits such as public exposure, liquidity for investors, and flexibility in offering structures, making it an ideal financing option to scale quickly and efficiently.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Because {n} has already raised {preraise} in pre-capital, utilizing a Reg A+ could be strategic. The pre capital can be used to scale its operations, expand its product offerings, and enhance its market presence while the Reg A+ is being offered and could potentially bring in significant funding. 
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Because {n} has already raised {preraise} through a {premarket}, utilizing a Reg A+ would be a logical next step that would allow the company to raise much more than previous investment types. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Reg A+ allows businesses to raise up to $75 million in a 12-month period, which is more than sufficient for your goal of raising {raisegoal}.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Because {n} is engaged in the {rounds} of capital raising, a Reg A+ offering is one of the best for high growth startups. It enables you to raise significant capital from a broad base of investors (both accredited and non-accredited), provides flexible terms, and allows you to structure your offering to align with your business goals. Additionally, it provides access to funds within a reasonable timeframe.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    A Reg A+ offering allows you to structure the funding in multiple rounds (or tranches). This means you can raise the $550,000 in {tranch} tranches as planned, ensuring flexibility in how you manage investor participation. You can launch one tranche, reach a certain milestone or valuation, and then proceed to the second tranche when you're ready.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Regulation A+ offerings are flexible, and there are no restrictions on how funds are used. This matches your need to use funds across various business needs. You will need to clearly outline these uses in the offering document (Form 1-A) to ensure full compliance and transparency with investors. You can use the raised capital for: {useoffund}
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Since Regulation A+ allows both accredited and non-accredited investors to participate, you can target investors with a higher risk tolerance, which is common for growth-stage businesses. The ability to raise capital from a broad pool of investors aligns well with your need to attract capital from investors who are willing to take on greater risk in exchange for potentially higher returns.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The principle’s tolerance for higher capital costs allows the company to effectively manage the expenses associated with such a public offering and leverage the funds to drive strategic growth and position the company for long-term success.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The typical costs of a Regulation A+ offering can range from $25,000 to $100,000 or more, depending on complexity and professional services required. However, if you are willing to spend between {upfrontcost}, this amount could be enough for some basic preparatory steps, such as legal and consulting advice, but you may need to consider increasing the budget to cover all necessary regulatory filings, legal review, and marketing.
    <br>Keep in mind that a self-underwritten offering might allow you to keep costs lower, but there could still be unavoidable expenses for legal filings (SEC filing fees), due diligence, and promotional activities. So, your budget might need to be adjusted unless you are planning to handle certain tasks yourself.</p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    A Reg A+ offering can be completed relatively quickly compared to traditional methods like an IPO. On average, it can take between 3 to 6 months from preparation to launch. The timeline can be faster if you have already established some groundwork or a network of interested investors.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)