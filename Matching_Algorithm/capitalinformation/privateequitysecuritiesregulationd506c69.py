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


def privateequitysecuritiesregulationd506c(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Rule 506(c) of Regulation D (Title II of the JOBS Act)</center></p>
    <p><b><u>Introduction</u></b><br>
    <a href="https://www.whitmanlegalsolutions.com/blog/2024/rule/506/real/estate">According to the SBAO Report, Rule 506(c), was used to raise only $169 Billion, with a median
    raise of only $750,000</a>. The number of “accredited” investors swelled to 24 million in 2022, the
    SEC said. <a href ="https://www.cnbc.com/2023/12/19/inflation-adds-millions-of-new-accredited-investors-sec-says.html">That’s 8 million more than in 2019, and the number is poised to keep growing.</a></p>

    <p><b><u>Definition of Capital Type</b></u><br> 
    1) Rule 506(c) permits issuers to broadly solicit and generally advertise an offering, provided
    that:
    <br>• all purchasers in the offering are accredited investors
    <br>• the issuer takes reasonable steps to verify purchasers’ accredited investor
    <br>• certain other conditions in Regulation D are satisfied</p>
                             
    <p>Purchasers in a Rule 506(c) offering receive “restricted securities” A company is required to file
    a notice with the Commission on Form D within 15 days after the first sale of securities in the
    offering. Although the Securities Act provides a federal preemption from state registration and
    qualification under Rule 506(c), the states still have authority to require notice filings and collect
    state fees. (SEC, 2024)</p>
                             
    <p>2) Regulation D (Reg D) 506(c) allows companies to sell securities through private placements
    without registering with the SEC, but they must comply with specific requirements. Unlike Reg
    D 506(b), which only permits sales to accredited investors without advertising, Reg D 506(c) lets
    companies market to everyone. Still, it requires them to verify that all purchasers are accredited
    investors. They must check income or net worth through documents like tax returns or bank
    statements. Issuers must file Form D with the SEC within 15 days after their first sale. While
    Reg D 506(c) offers more opportunities, verifying investors requires more diligence.</p>
                             
    <p>Accredited investors must meet certain financial thresholds, such as having a minimum net worth
    of $1 million or an annual income of $200,000 for individuals ($300,000 for joint income with a
    spouse) for the past two years with a reasonable expectation of the same income criteria in the
    present year.</p>
                             
    <p>The investors involved in a Reg D 506(c) offering are typically sophisticated and financially
    experienced, consisting of institutional investors, high-net-worth individuals, venture capital
    firms, private equity firms, and other sophisticated investors who are capable of conducting their
    due diligence and evaluating the risks and rewards of private placements. Issuers of securities in
    a Reg D 506(c) offering must take reasonable steps to verify the accredited investor status of
    their investors.</p>
                             
    <p>Regulation D Rule 506(c) allows issuers to avoid registration with the Securities and Exchange
    Commission (SEC) by meeting specific qualifications and verifying that investors are accredited.
    This approach is ideal for raising larger amounts of funds quickly and gaining access to
    sophisticated investors who are more likely to invest in private offerings. Reg D 506(c) reduces
    compliance-related challenges associated with public offerings and crowdfunding campaigns,
    making fundraising easier and less costly for smaller companies looking to grow their businesses
    and investor bases. (RegD 506c, n.d.)</p>
                             
    <p>3)Purchasers of securities offered pursuant to Rule 506 receive “restricted” securities, meaning
    that the securities cannot be sold for at least six months or a year without registering them.
    506(c)’s defining feature: A GP can perform general solicitation and advertising without any
    limitation on how much capital they can raise.</p>
                             
    <p>How 506(c) investors can verify LP accreditation<br>
    • If an LP is claiming accreditation based on income, the GP may need to obtain the LP’s
    tax forms for the previous two years. GPs also would have to obtain confirmation that the LP’s
    income will continue to meet the minimum threshold for accredited investors (which is $200,000
    annually for an individual and $300,000 for a married couple) in the current year.
    <br>• If the LP claims accreditation based on net worth, GPs can review the LP’s assets by
    collecting proof of the purchaser’s assets and liabilities (for example, bank statements and
    brokerage reports) within the past three months. GPs must also obtain confirmation from the LP
    that all liabilities that could impact net worth have been disclosed. To be an accredited investor,
    an individual must have a net worth of more than $1 million, excluding their primary residence.
    <br>• If the LP claims accreditation based on one of the SEC’s recognized professional
    certifications, the GP would need to obtain a copy of that certification.</p>
                             
    <p>GPs may also get written confirmation from the investor’s attorney, broker dealer, registered
    investment advisor, or CPA confirming they took reasonable steps to verify the investor’s
    accreditation status in the past three months.<br>
    Once the fund manager verifies an investor’s accredited status, the investor can self-certify as an
    accredited investor with that GP for a period up to five years, assuming the GP doesn’t become
    aware of information to the contrary within that timespan.<br>
    506(c) benefits:<br>
    • Rule 506(c) offerings are not subject to state blue-sky laws.
    <br>• GPs can publicly market their capital-raising offer to a larger investor base, beyond just
    one-on-one conversations and emails within their personal and professional networks.
    506(c) limitations:
    <br>• Verifying accredited investors takes up time and money.
    <br>• Many investors are reluctant to give sensitive information to GPs they don’t have a
    personal relationship with.
    <br>• Given the potential liability third parties take on when they certify investor accreditation,
    accountants and lawyers are unlikely to make these certifications except perhaps for very large,
    lucrative clients.
    <br>Due to these limitations, GPs with robust networks of accredited investors often seek to avoid
    compliance costs and regulatory risks by raising money under Rule 506(b). On the flip side,
    emerging GPs without an established network of accredited investors could benefit from raising
    as a 506(c) because it allows them to solicit investors via social media, print advertising, or
    marketing. (Rule 506 of Regulation D, n.d.)</p>
    <p><b><u>References</u></b><br>
    RegD 506c. (n.d.). Retrieved from Syndication Pro: <a href="https://syndicationpro.com/glossary-
    definitions/regd-506c">https://syndicationpro.com/glossary-
    definitions/regd-506c</a></p>
                             
    <p>Rule 506 of Regulation D. (n.d.). Retrieved from Investor.gov:
    <a href="https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-506-regulation-d">https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-506-regulation-d</a></p>
                             
    <p>SEC. (2024, June 28). General solicitation — Rule 506(c). Retrieved from SEC:
    <a href="https://www.sec.gov/resources-small-businesses/exempt-offerings/general-solicitation-rule-506c">https://www.sec.gov/resources-small-businesses/exempt-offerings/general-solicitation-rule-506c</a>
    </p>
    <p><u><b>Legal Qualification Requirements</u></b>
    <br>• Be a Private or Public U.S. Company or Foreign Entity
    <br>• Companies offering 506 (c) investments can perform "general solicitation" openly and
    freely, ads on the internet, social media, print, etc
    <br>• All investors must be accredited
    <br>• Accredited investors must be verified
    <br>• Accredited investors can invest an unlimited amount
    <br>• Sells "restricted securities"
    <br>• Can sell securities of any type
    <br>• File Form D with the SEC within 15 days of the first sale of securities
    <br>• Ensure none of the executives, directors, or significant shareholders are disqualified as
    bad actors
    <br>• The company must ensure that all statements and disclosures made to investors are
    truthful and complete
    <br>• The company must disclose how it plans to use the proceeds from the offering
    <br>• While the company is not required to provide audited financials for offerings under Rule
    506(c), it must provide accurate financial statements (balance sheets, income statements, etc.),
    which may be reviewed by investors and regulators
    <br>• The offering must comply with the overall requirements of the Securities Act of 1933,
    including ensuring that no misleading statements are made and that all material information is
    disclosed to potential investors
    <br>• Not required to comply with Blue Sky Laws</p>
    
    <p><b><u>Supporting Document List</u></b>
    <br>• Form D Filing
    <br>• Accredited Investor Verification Documents: Investor questionnaires, Financial
    documents (e.g., tax returns, bank statements, and proof of income or assets)
    <br>• Third-party verification: Obtaining written confirmation from a third-party professional
    (CPA, attorney, or broker-dealer) who can verify investor accreditation.
    <br>• Subscription Agreement: A signed agreement between the company and investors
    outlining the terms of the investment, including the amount to be invested, type of securities
    being purchased, and other pertinent conditions.
    <br>• Company Organizational Documents: Articles of Incorporation or equivalent
    organizational documents. Bylaws, Operating Agreement, or other governing documents. Board
    of Directors’ resolutions or shareholder approval (if required).
    <br>• Investor Risk Disclosures: A document detailing the risks involved in the investment,
    ensuring that investors are fully aware of the potential downsides and uncertainties of the
    offering.
    <br>• Private Placement Memorandum (PPM): Although not required, it is highly
    recommended to prepare a Private Placement Memorandum to disclose all relevant details about
    the offering, including risks, company financials, and terms of the securities.
    <br>• Financial Statements: Financial statements for the company, including balance sheets,
    income statements, and cash flow statements. For larger offerings, audited financials may be
    required.
    <br>• Marketing and Solicitation Materials: Copies of any marketing materials or
    advertisements used to promote the offering, ensuring they comply with SEC regulations and
    accurately present the offering.
    <br>• Use of Proceeds Statement: A detailed explanation of how the capital raised will be used,
    such as for business development, operations, or other specific needs.
    <br>• Investor Accreditation Process Documentation in compliance with SEC guidelines.</p>                                                                           
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506cfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Equity Securities<br>
    Capital Type: Rule 506(c) of Regulation D (Title II of the JOBS Act)</center></p>                        
    <p><center><u><b>Frequently Asked Question for Regulation D 506(c)</u></b></center></p>
                             
    <p><u><b>1. What is Rule 506(c) of Regulation D?</u></b><br>
    •Answer: Rule 506(c) allows companies to raise capital through private offerings while
    advertising the offering to the general public. However, all investors must be accredited
    investors (i.e., those who meet certain financial criteria set by the SEC).</p>
                             
    <p><u><b>2. What are the key advantages of using Rule 506(c)?</u></b><br>
    • Answer: 
    <br>- General solicitation and advertising: Unlike other private offerings, Rule 506(c)
    allows companies to advertise and publicly solicit investments through channels like
    social media, websites, and other public platforms.
    <br>- Access to a larger pool of investors: By allowing general solicitation, companies can
    potentially reach more accredited investors, which could lead to faster fundraising.
    <br>- No limit on capital raised: Companies can raise any amount of capital without restriction,
    provided they only accept investments from accredited investors.</p>
                             
    <p><u><b>3. What is an accredited investor?</u></b><br>
    • Answer: An accredited investor is an individual or entity that meets specific financial
    criteria set by the SEC, such as:<br>
    • Individuals: Net worth of $1 million (excluding primary residence) or annual income of
    $200,000 ($300,000 with a spouse) in the last two years, with expectations to maintain
    those levels.
    • Entities: Certain institutional investors, such as banks, insurance companies, and
    investment companies with more than $5 million in assets.</p>
                             
    <p><u><b>4. What is the process for verifying accredited investors under Rule 506(c)?</u></b><br>
    • Answer:  Companies are required to take reasonable steps to verify that all investors are
    accredited. This can be done by reviewing documents such as:
    <br>- Tax returns, bank statements, or brokerage statements
    <br>- Written confirmations from a third party (e.g., a CPA or attorney)
    <br>- Investment letters or other verifiable documentation.
    <br>- The SEC provides guidance on what constitutes “reasonable steps,” but businesses have
    flexibility in how they verify accredited status.</p>
                             
    <p><u><b>5.Can I use general advertising and solicitation for my offering?</u></b><br>
    • Answer: Yes, Rule 506(c) permits general solicitation and advertising. You can use
    websites, social media, press releases, and other forms of advertising to promote your
    offering to a wide audience, as long as you ensure all investors are accredited.</p>
                             
    <p><u><b>6. Are there any restrictions on who can invest in a Rule 506(c) offering?</u></b><br>
    • Answer: Yes, all investors must be accredited investors. The company cannot accept
    investments from non-accredited investors, unlike other forms of capital raising (e.g.,
    Regulation Crowdfunding or Regulation A).</p>
                             
    <p><u><b>7. How do I file with the SEC for a Rule 506(c) offering?</u></b><br>
    • Answer: While Rule 506(c) offerings are exempt from full SEC registration, companies
    must still file a Form D with the SEC within 15 days of the first sale of securities. Form
    D provides notice of the offering and claims the exemption from registration under
    Regulation D.
    </p>
                             
    <p><u><b>8.What are the costs associated with using Rule 506(c)?</u></b><br>
    • Answer:  The costs for Rule 506(c) offerings can include:
    <br>- Legal and compliance fees for preparing offering documents and verifying accredited
    investors
    <br>- Marketing and advertising expenses to promote the offering
    <br>- Filing fees for submitting Form D with the SEC
    <br>- Brokerage or intermediary fees if using a platform or network to connect with accredited
    investors.</p>
                             
    <p><u><b>9. How is a Rule 506(c) offering different from Rule 506(b) of Regulation D?</u></b><br>
    • Answer: 
    <br>- Rule 506(c) allows general solicitation and requires that all investors are
    accredited investors.
    <br>- Rule 506(b) does not allow general solicitation or advertising, but allows companies to
    raise funds from up to 35 non-accredited investors in addition to accredited investors.
    <br>- Rule 506(c) is more flexible for reaching a broader audience but limits investment to
    accredited investors only.
    </p>
                             
    <p><u><b>10. How does the use of general solicitation impact investor relations?</u></b><br>
    • Answer:Using general solicitation means that you can openly advertise your offering,
    potentially attracting more investors. However, it also means that you must take extra
    care to vet investors, ensuring they are accredited. It’s important to build a strong and
    professional reputation to attract serious investors.
    </p>
                             
    <p><u><b>11. What is the maximum amount I can raise using Rule 506(c)?</u></b><br>
    • Answer: There is no limit to the amount of capital you can raise under Rule 506(c), as
    long as all investors are accredited. This makes it an attractive option for companies that
    need to raise significant capital.
    </p>
                             
    <p><u><b>12. Can I continue to raise funds in multiple rounds under Rule 506(c)?</u></b><br>
    • Answer: yes, companies can conduct multiple rounds of fundraising under Rule 506(c),
    provided they follow the rules for general solicitation, maintain investor verification, and
    file the necessary Form D updates for each round.
    </p>
                             
    <p><u><b>13. What are the investor protections in a Rule 506(c) offering?</u></b><br>
    • Answer: While there are no special protections under Rule 506(c) for investors, the
    company must ensure that all disclosures are accurate and complete. The SEC’s anti-
    fraud provisions apply, meaning the company must not mislead investors through false or
    omitted information.
    </p>
                             
    <p><u><b>14. Can I offer equity or debt under Rule 506(c)?</u></b><br>
    • Answer:  Yes, you can offer equity (e.g., common stock or preferred stock) or debt (e.g.,
    convertible notes or bonds) under Rule 506(c), as long as the offering complies with the
    accredited investor requirement and other applicable regulations</p> 
                             
    <p><u><b>15. Do I need to provide disclosures to investors in a Rule 506(c) offering?</u></b><br>
    • Answer: Yes, while the offering is exempt from full SEC registration, companies are still
    required to provide detailed disclosures to investors. This includes information about the
    company’s financials, risk factors, use of proceeds, and the terms of the offering, similar
    to what would be required in a registered offering.
    </p>
                             
    <p><u><b>16. Can a company use Rule 506(c) for international investors?</u></b><br>
    • Answer:Yes, Rule 506(c) can include international accredited investors, but companies
    must ensure compliance with U.S. securities laws and any applicable laws in the
    investor’s country. This may involve additional legal considerations and verifications.
    </p>

    <p><u><b>17. What happens if a company violates the general solicitation rules?</u></b><br>
    • Answer: Violating the general solicitation rules could result in the company losing its
    exemption under Regulation D, meaning the offering would be considered a public
    offering that requires SEC registration. This could expose the company to penalties, fines,
    and legal liabilities.
    </p>                                                                                                                
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506ctwelve(request):
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
    Private Equity Rule 506(b) of Regulation D (Title II of the JOBS Act)</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    While {n} is in the {stage} stage, utilizing Private Equity Rule 506(c) of Regulation D
    (Title II of the JOBS Act) offers several strategic advantages. Rule 506(c) is ideal for companies
    in the {stage} stage looking to scale operations, engage a network of accredited investors, and
    raise funds more efficiently while maintaining compliance with SEC regulations. Rule 506(c)
    enables you to target high-net-worth individuals and institutional investors, offering greater
    flexibility in structuring your offering.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Utilizing Private Equity Rule 506(c) of Regulation D (Title II of the JOBS Act) for a {entity}
    provides flexibility in terms of funding structure and investor outreach, with fewer
    regulatory burdens compared to traditional methods like venture capital or an IPO. It also
    enables you to engage a targeted investor pool, which is ideal for scaling the business quickly
    and efficiently while maintaining compliance with SEC regulations.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    {n} has already raised {preraise} in pre-capital so continuing raising capital utilizing
    Private Equity Rule 506(c) of Regulation D (Title II of the JOBS Act) offers flexibility in
    structuring the offering and the ability to publicly advertise, which significantly expands the
    pool of potential investors.   
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    {n} has already raised {preraise} through a {premarket} so utilizing Private Equity Rule
    506(c) of Regulation D (Title II of the JOBS Act) offers faster access to significant capital
    compared to traditional fundraising routes, enabling Dining Empire to effectively engage with a
    targeted group of investors while scaling its operations.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Private Equity Rule 506(c) of Regulation D (Title II of the JOBS Act) allows businesses to raise 
    an unlimited amount of capital from accredited investors over a 12-month period, providing significant 
    flexibility for your goal of raising {raisegoal}.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    While {n} is engaged in the {rounds} of capital raising, Private Equity Rule 
    506(c) of Regulation D (Title II of the JOBS Act) allows you to raise funds exclusively from accredited 
    investors, offering access to a high-net-worth investor base. This targeted investor pool is a key advantage. 
    The capital raised can be used for scaling operations, marketing, and growing human capital, making Rule 
    506(c) a strong option for early-stage businesses looking to raise substantial capital and 
    accelerate growth.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Since you're planning to raise capital in {tranch} tranches within a 12-month period, Private Equity
    Rule 506(c) of Regulation D (Title II of the JOBS Act) offers the flexibility to structure your
    offering in multiple stages, allowing you to align the fundraising process with your specific
    business needs and funding objectives.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Private Equity Rule 506(c) of Regulation D (Title II of the JOBS Act) offers significant
    flexibility in how funds raised can be used, with no specific restrictions on their allocation. This
    makes it an ideal solution for addressing the diverse financial needs of your business. While you
    will need to clearly specify these intended uses in the offering documents to ensure compliance
    and transparency with investors, Rule 506(c) allows you to raise capital for purposes such as:<b>note(should be used from this list: {useoffund})</b>
    <br>1. Startup – Working Capital
    <br>2. Growth Scalability
    <br>3. Marketing & Sales
    <br>4. Cash Flow Capital
    <br>5. Human Capital
    <br>6. Other</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Private Equity Rule 506(c) of Regulation D (Title II of the JOBS Act) allows you to present an
    investment opportunity to a targeted group of investors who are typically seeking higher returns
    and are interested in high-growth, early-stage companies. This aligns well {n}
    growth objectives. Under Rule 506(c), you have the flexibility to offer various types of securities
    depending on what best fits your business model and investor preferences. Since your company
    has already raised capital through {premarket}, you can continue with this structure or choose to offer
    equity in exchange for the capital raised.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The principle’s willingness to accept {enterprisecost} costs enables the company to manage the 
    expenses associated with a public offering under Private Equity Rule 506(b) of Regulation D 
    (Title II of the JOBS Act), while leveraging the funds to drive strategic growth, broaden the 
    investor base, and position the company for long-term success. This approach provides the 
    flexibility to engage with investors who are typically seeking higher returns.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>With a {upfrontcost} budget, Rule 506(c) of Regulation D may be a challenging option unless
    you are able to leverage existing networks of accredited investors and manage legal, marketing,
    and verification costs efficiently. For smaller budgets, Regulation CF or other private placements
    might be more feasible options to raise capital while keeping expenses manageable.
    Low-end estimate: $10,000 - $15,000 (with minimal legal and marketing involvement)
    High-end estimate: $30,000 - $50,000 or more (with a full-scale offering, legal representation,
    investor verification, platform usage, and marketing)
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>The capital-raising process under Rule 506(c) of Regulation D can typically take 3 to 6 months
    depending on how efficiently you manage the preparation, marketing, and investor verification
    processes. It could take as little as {upfronttime} if you already have a solid investor network and
    streamlined processes in place, but be prepared for a longer timeline if you're starting from
    scratch or targeting a larger pool of investors.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)