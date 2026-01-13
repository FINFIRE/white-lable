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
#done

def privateequitysecuritiesregulationCFtitleIII(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation CF Title III</center></p>
    <p><b><u>Introduction</b></u><p>
    <p>Reg CF (Title III) is ideal for companies raising equity capital in amounts up to $5 million dollars in a given 12-month period of time. It is designed so that privately held companies can raise money from the general public through SEC-registered crowdfunding platforms. {n} fits that definition. Reg CF has been a viable funding option for businesses since 2016, following its implementation under the JOBS Act. For example, in 2023, more than $494 million was raised through Regulation Crowdfunding offerings. As of mid-2024, over 6,000 companies have utilized Reg CF to reach a broader investor base online. The average raise in 2023 was approximately $471,000, showcasing the regulation's appeal to early-stage startups and smaller businesses. While Reg CF expands access to capital, companies should also be aware of potential risks, including complex disclosure requirements, annual reporting obligations, and investment limits based on investor income and net worth.</p>
    <p><b><u>Definition of Capital Type</u></b></p>
    <p>1) Regulation Crowdfunding enables eligible companies to offer and sell securities through
    crowdfunding. The rules include:</p>
    <p>• Require all transactions under Regulation Crowdfunding to take place online through an
    SEC-registered intermediary, either a broker-dealer or a funding portal
    <br>• Permit a company to raise a maximum aggregate amount of $5 million through
    crowdfunding offerings in a 12-month period
    <br>• Limit the amount individual non-accredited investors can invest across all crowdfunding
    offerings in a 12-month period
    <br>• Require disclosure of information in filings with the Commission and to investors and the
    intermediary facilitating the offering.
    <br>Securities purchased in a crowdfunding transaction generally cannot be resold for one year.
    Regulation Crowdfunding offerings are subject to "bad actor" disqualification provisions. (SEC,
    Regulation Crowdfunding, 2024)</p>
    <p>2) Crowdfunding falls under securities laws allowing it to be used to offer and sell securities.
    Crowdfunding permits individuals to invest in securities-based crowdfunding transactions subject
    to certain investment limits. The rules also limit the amount of money an issuer can raise using the
    crowdfunding exemption, impose disclosure requirements on issuers for certain information about
    their business and securities offering, and create a regulatory framework for the broker-dealers and
    funding portals that facilitate the crowdfunding transactions.</p>
    <p>Regulation Crowdfunding permits a company to raise a maximum aggregate amount of $5,000,000
    through crowdfunding offerings in a 12-month period. Non-accredited investors are limited in the
    amounts they are allowed to invest in all Regulation Crowdfunding offerings over the course of a
    12-month period.</p>
    <p>If either of a non-accredited investor’s annual income or net worth is less than $124,000, then the
    investor’s investment limit is the greater of:</p>
    <p>$2,500 or 5 percent of the greater of the non-accredited investor’s annual income or net worth.
    If both annual income and net worth are equal to or more than $124,000, then the non-accredited
    investor’s limit is 10 percent of the greater of their annual income or net worth.</p>

    <p>During any 12-month period, the aggregate amount of securities sold to a non-accredited investor
    through all Regulation Crowdfunding offerings may not exceed $124,000, regardless of the non-
    accredited investor’s annual income or net worth. Spouses are allowed to calculate their net worth
    and annual income jointly.</p>
    <p>One of the key investor protections of Title III of the JOBS Act is the requirement that Regulation
    Crowdfunding transactions take place through an SEC-registered intermediary, either a broker-
    dealer or a funding portal. Under Regulation Crowdfunding, offerings must be conducted
    exclusively through a platform operated by a registered broker or a funding portal. The rules
    require these intermediaries to:</p>
    <p>• Provide investors with educational materials.
    <br>• Take measures to reduce the risk of fraud.
    <br>• Make issuer and offering information available.
    <br>• Provide communication channels to permit discussions about offerings on the platform;
    and
    <br>• Facilitate the offer and sale of crowdfunded securities.
    The rules prohibit funding portals from:
    <br>• Offering investment advice or recommendations.
    <br>• Soliciting purchases, sales or offers to buy securities offered or displayed on its platform.
    <br>• Compensating promoters and others for solicitations or based on the sale of securities; and
    <br>• Holding, possessing, or handling investor funds or securities.</p>
    <p>The rules provide a safe harbor under which funding portals can engage in certain activities
    <p>consistent with these restrictions. (Smith, 2021)</p>
    Prior to filing a Form C, a crowdfunding issuer may “test the waters,” or solicit interest in a
    potential offering from the general public, orally or in writing, provided that the solicitation
    materials state:</p>
    <p>No money or other consideration is being solicited, and if sent in response, will not be accepted;</p>
    <p>No offer to buy the securities can be accepted and no part of the purchase price can be received
    until the issuer determines the exemption under which the offering is intended to be conducted
    and, where applicable, the filing, disclosure, or qualification requirements of such exemption are
    met; and</p>
    <p>A person’s indication of interest involves no obligation or commitment of any kind.</p>
    <p>Until the Form C is filed, solicitation or acceptance of money or other consideration, or of any
    commitment, binding or otherwise, from any person is prohibited. Any solicitation materials
    must be included with the Form C that is filed with the Commission. (SEC, Regulation
    Crowdfunding: Guidance for Issuers, n.d.)</p>
                             
    <u><b><p>References</u></b><br>
    SEC. (2024, November 14). Regulation Crowdfunding. Retrieved from SEC:
    <a href="https://www.sec.gov/resources-small-businesses/exempt-offerings/regulation-crowdfunding">https://www.sec.gov/resources-small-businesses/exempt-offerings/regulation-crowdfunding</a></p>
    <p>SEC. (n.d.). Regulation Crowdfunding: Guidance for Issuers. Retrieved from SEC:
    <a href="https://www.sec.gov/resources-small-businesses/regulation-crowdfunding-guidance-
    issuers#requirements">https://www.sec.gov/resources-small-businesses/regulation-crowdfunding-guidance-
    issuers#requirements</a></p>
    <p>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.</p>
    <p>Form C : <a href="https://www.sec.gov/about/forms/formc.pdf">https://www.sec.gov/about/forms/formc.pdf</a></p>
    <p>2015 Regulation Crowdfunding : <a href = "https://www.sec.gov/files/rules/final/2015/33-9974.pdf">https://www.sec.gov/files/rules/final/2015/33-9974.pdf</a></p>
    <p>In 2015, the Commission adopted Regulation Crowdfunding to implement the requirements of
    Title III. Under the rules, eligible companies were allowed to raise capital using Regulation
    Crowdfunding starting May 16, 2016.</p>
    <p>2020 Amendments to Regulation Crowdfunding</p>
    <p><a href="https://www.sec.gov/files/rules/final/2020/33-10884.pdf">https://www.sec.gov/files/rules/final/2020/33-10884.pdf</a></p>
    <p>On November 2, 2020, the Commission adopted certain amendments to Regulation
    Crowdfunding relating to the maximum offering amount, investor investment limits, special
    purpose vehicles, integration framework, and testing-the-waters communications.</p>
    <p><b><u>Legal Qualification Requirements</u></b></p>
    <p>• Be a U.S.-based, for-profit company.
    <br>• Have a well-defined operational business plan.
    <br>• Raise no more than $5 million in a 12-month period.
    <br>• Abide by investment limits for non-accredited investors.
    <br>• Conduct the offering through an SEC and FINRA registered crowdfunding platform.
    <br>• File a Form C with the SEC, including detailed disclosures about the company and the
    offering.
    <br>• Provide financial statements (audited or reviewed, depending on the offering size).
    <br>• Ensure that none of its officers, directors, or major shareholders are disqualified as bad
    actors.
    <br>• Follow ongoing reporting requirements which involve filing an annual report on Form C-
    AR with the SEC, including financial statements and updates on the company's progress,
    no later than 120 days after the end of the issuer's fiscal year; this report must also be
    posted on the issuer's website to keep investors informed about the business's progress
    and financial condition.</p>
    <p><b><u>Supporting Document List</u></b></p>
    <p>• Form C (Offering Statement) with company details, offering terms, use of proceeds, and
    financial disclosures.
    <br>• Financial Statements (audited or reviewed, depending on the amount raised).
    <br>• Offering Circular or Prospectus (if applicable).
    <br>• Consent to Use of Personal Information for officers, directors, and significant
    shareholders.
    <br>• Form U-2: Consent to Service of Process.
    <br>• State-Level Filings (if applicable, based on state laws).
    <br>• Investor Questionnaire (if required by the platform).
    <br>• Special Purpose Vehicle (SPV) Information (if applicable).
    <br>• Third-Party Due Diligence Reports (if provided).
    <br>• Conflict of Interest Disclosures.</p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationCFtitleIIIfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Equity Securities<br>
    Capital Type: Regulation CF Title III</center></p>                        
    <p><center><u><b>Frequently Asked Question for Regulation CF Title III</u></b></center></p>
    <p><u><b>1. What is Regulation Crowdfunding (Reg CF)?</u></b><br>
    • Answer: Reg CF is a provision of the JOBS Act that allows small businesses and startups
    to raise capital by offering equity or debt securities to a large number of investors,
    including both accredited and non-accredited investors, through SEC-registered
    crowdfunding platforms.</p>
                             
    <p><u><b>2. Why should my business consider using Reg CF to raise capital?</u></b><br>
    • Answer: Reg CF allows companies to raise up to $5 million in a 12-month period. It
    provides access to a wide range of investors, including non-accredited individuals, and
    offers an opportunity to engage your customer base or community in your business.
    Unlike venture capital or angel investing, Reg CF is more accessible and can be less
    time-consuming for companies that don't want to give up too much equity or control.</p>
                             
    <p><u><b>3. Who can invest in my Reg CF offering?</u></b><br>
    • Answer: Both accredited and non-accredited investors can participate in a Reg CF
    offering. However, non-accredited investors have investment limits based on their
    income or net worth (i.e., up to $2,200 or 5-10% of their annual income or net worth,
    depending on the amount they make or own). Accredited investors are not subject to
    these limits.</p>
                             
    <p><u><b>4. How much capital can my business raise through Reg CF?</u></b><br>
    • Answer: Under Reg CF, your business can raise up to $5 million in a 12-month period.
    This limit applies to all capital raised through crowdfunding offerings, including
    offerings made on different platforms.</p>
                             
    <p><u><b>5. What types of securities can be offered through Reg CF?</u></b><br>
    • Answer: You can offer equity (e.g., common or preferred stock) or debt securities (e.g.,
    convertible notes) through Reg CF. The specific type of security you choose will depend
    on your company's goals, investor appetite, and the terms of your offering.</p>
                             
    <p><u><b>6. What is the process for raising funds through Reg CF?</u></b><br>
    • Answer: The process involves:<br>
    1. Choosing a registered crowdfunding platform: You must use an SEC-registered
    platform to conduct your offering.<br>
    2. Filing Form C with the SEC: This form includes details about your company, the
    offering terms, financial statements, and risk factors.<br>
    3. Marketing your offering: You can share your offering with your network and
    potential investors via the platform, but the marketing must comply with SEC
    rules.<br>
    4. Raising funds: Investors can commit to your offering through the platform.<br>
    5. Closing the offering: Once you reach your fundraising goal, the offering closes,
    and you receive the funds.</p>
                             
    <p><u><b>7. What are the cost associated with using Reg CF?</u></b><br>
    • Answer: There are several costs to consider, including:<br>
    - Platform fees: Crowdfunding platforms typically charge a fee ranging from 3-7%
    of the total capital raised.<br>
    - Legal and accounting fees: Preparing the necessary filings with the SEC (Form C)
    and providing financial statements can incur legal and accounting costs.<br>
    - Marketing costs: Promoting the offering can require additional marketing efforts,
    potentially incurring costs for digital advertising, public relations, etc.</p>
                             
    <p><u><b>8. What are the ongoing compliance requirements after the offering?</u></b><br>
    • Answer: Once your offering is completed, you are required to comply with ongoing
    reporting requirements:<br>
    - Annual reports: You must file annual reports with the SEC, which include
    updated financial statements (audited if applicable).<br>
    - Updates to investors: You must provide regular updates to your investors about
    the business’s progress, material changes, and financial condition.<br>
    - These obligations are in place to keep investors informed and maintain
    transparency.</p>
                             
    <p><u><b>9. What are the risks of raising capital through Reg CF?</u></b><br>
    • Answer: Some potential risks include:<br>
    - Dilution: Offering equity will dilute the ownership of existing shareholders.<br>
    - Compliance: Ensuring that you comply with all SEC and state regulations,<br>
    including filing forms, financial disclosures, and reporting, can be complex and
    time-consuming.<br>
    - Investor relations: You may have to manage a large number of investors, which
    can lead to additional administrative and communication burdens.<br>
    - Public exposure: Your business will be publicly disclosing financial and strategic
    information, which could attract unwanted attention or competitors.</p>
                             
    <p><u><b>10. What are the eligibility requirements to raise funds through Reg CF?</u></b><br>
    • Answer: To be eligible for Reg CF, your company must:<br>
    - Be a U.S.-based entity (for-profit).<br>
    - Not have already raised more than $5 million in the past 12 months through other
    crowdfunding or securities offerings.<br>
    - File Form C with the SEC, including detailed information about your company,
    financials, and risks.<br>
    - Use an SEC-registered crowdfunding platform for the offering.</p>
                             
    <p><u><b>11. How long does it take to complete a Reg CF offering?</u></b><br>
    • Answer: The timeline can vary, but typically, a Reg CF offering can take between 1-3
    months to complete. This includes time for preparing and filing Form C, marketing the
    offering, and closing the funding round. The process may be quicker or longer depending
    on how well the offering is marketed and the amount of capital you are trying to raise.</p>
                             
    <p><u><b>12. Can I raise capital through Reg CF and other methods at the same time?</u></b><br>
    • Answer: Yes, you can raise capital from multiple sources (e.g., venture capital, angel
    investors, or other crowdfunding methods) at the same time, but the $5 million Reg CF
    cap applies to the total amount raised across all methods within a 12-month period.
    Additionally, you must disclose other capital raises in your offering materials.</p>
                             
    <p><u><b>13. What happens if I do not reach my fundraising goal?</u></b><br>
    • Answer: Reg CF offerings must be conducted on a “all-or-nothing” basis. If you do not
    reach the minimum funding goal specified in your offering, the funds are returned to
    investors, and the offering is considered a failure. However, if you successfully raise the
    targeted amount, the funds are transferred to your company.</p>
                             
    <p><u><b>14. Can I cancel or modify my Reg CF offering?</u></b><br>
    • Answer: Once your offering has launched and investors have committed to the offering, it
    is typically difficult to change or cancel the terms. If you want to modify the offering
    after it has been launched, you will likely need to re-file with the SEC, which could delay
    the offering or lead to potential legal challenges. Therefore, it’s important to thoroughly
    plan and finalize all offering details</p> 
    beforehand.
                             
    <p><u><b>15. What is the role of the crowdfunding platform in Reg CF?</u></b><br>
    • Answer: The crowdfunding platform serves as the intermediary between the business
    raising funds and the investors. The platform must be SEC-registered and FINRA-
    member and is responsible for:<br>
    - Facilitating the offering process.<br>
    - Ensuring the company complies with Reg CF rules.<br>
    - Hosting the offering information and providing tools for investors to commit
    funds.<br>
    - Ensuring that the business meets the SEC’s filing requirements.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationCFtitleIIItwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT</b></u><br>
    Regulation Crowdfunding Title III</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    {n} is in an {stage} stage. Equity Securities Regulation CF (Reg CF) offers several
    strategic advantages to startups and early-stage businesses in their growth stage. The initial costs
    are relatively low (Fees are mostly assessed at the back end); documentation requirements are
    not solely based on valuation, sales, financial statements, which are usually challenging
    requirements for early-stage companies. Minimum fund raise amounts are established based on
    the back end fees that need to paid ($15,000 to $30,000). Reg CF can be a path for companies in
    the growth stage looking to scale their operations, build a community of investors, and attract a
    diverse group of supporters with varying levels of investment, but is primarily for startups.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Regulation CF (Title III) is best suited for C Corporations, possibly an “S” Corp, less of a match
    for Limited Liability Companies (But is possible). Reg CF is not appropriate for any other entity
    type. Reg CF, by definition, will be selling equity (Stock or member units), which is why a sole
    proprietor cannot utilize Reg CF. Regulation CF provides valuable benefits such as increased
    visibility through crowdfunding platforms, engagement with a community of investors, and
    flexibility in offering structures, making it an ideal financing option to scale quickly and
    efficiently.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    The amount of money raised prior to a Regulation CF is immaterial and does not affect the
    match, except cases wherein the company has already raised in excess of $5 Million, and in that
    case, Reg CF is not an appropriate capital type, in most cases. Because {n} has already
    raised pre-capital, utilizing a Private Equity Securities Regulation CF (Title III) is a good fit and
    allows for a broader and more diverse investor pool (both accredited and non-accredited), lower
    fundraising costs, and flexibility in funding structures. Some of the previously raised capital may
    be used to market to new investors. These advantages are especially important for a growing
    company looking to scale its operations, expand its product offerings, and enhance its market
    presence, while also engaging directly with a community of investors who are invested in its
    success.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Because {n} has already raised {preraise} through {premarket}<b>(note:use for loop here to present all the item of least letter)</b> utilizing a Private Equity Securities Regulation CF (Title III) is a natural next step in the
    fund-raising process.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Regulation CF allows businesses to raise up to $5 million in a 12-month period, which is more
    than sufficient for your goal of raising {raisegoal}. This provides an ideal opportunity to access
    capital while engaging a diverse investor base through crowdfunding platforms.These include the ability to raise capital (up to $5 million), access a wide pool of investors (both
    accredited and non-accredited), and engage in crowdfunding to increase visibility.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    For a C Corporation engaged in the {rounds} of capital raising, a Private Equity
    Securities Regulation CF (Title III) offering allows you to raise funds from a wide range of
    investors, including both accredited and non-accredited individuals. This flexibility in investor
    base is a key advantage. Regulation CF also offers customizable terms, enabling you to structure
    the offering in a way that aligns with your specific business objectives. Compared to an IPO,
    Regulation CF has lower regulatory burdens and provides faster access to capital through
    crowdfunding platforms. Additionally, it offers a unique opportunity to engage directly with a
    broad community of investors.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Since you're planning to raise capital in {tranch} tranches within a 12-month period, Regulation CF
    is a good fit for that goal as all the funds can be raised in one crowdfunding campaign.</p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Regulation CF offerings are flexible, with no restrictions on how the funds are used, making it an
    ideal option for meeting your diverse business needs. This flexibility provides you with the
    ability to use the funds as needed to support different aspects of your business While you’ll need
    to clearly outline these uses in the offering documents to ensure full compliance and
    transparency with investors, Regulation CF allows you to raise capital for: <b>note(should be used from this list: {useoffund})</b>
    1. Startup - Working Capital - note should be updated from the list
    2. Growth Scalability - note should be updated from the list
    3. Marketing & Sales - note should be updated from the list
    4. Cash Flow Capital - note should be updated from the list
    5. Human Capital - note should be updated from the list
    6. Other - note should be updated from the list</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Regulation CF is designed for start-ups and early-stage companies with a high degree of risk.
    It allows you to present an investment opportunity to a wide range of individuals who are
    interested in early-stage, high-growth companies. These investors are typically seeking higher
    returns, which aligns with your company’s growth stage. Under Regulation CF, you can offer
    various types of securities, such as equity, convertible notes, or SAFEs, depending on what best
    suits your business model and investor preferences. Since your company has already raised
    capital through {premarket}, you can continue with a similar structure or offer equity in exchange for
    capital raised through the crowdfunding campaign, engaging a broad base of investors while
    scaling your business.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The founder’s willingness to accept {enterprisecost} costs enables the company to efficiently
    handle the expenses tied to a public offering under Regulation CF, while using the funds to drive
    strategic growth, expand the investor base, and position the company for sustained success. The
    good news is that the majority of Reg CF fees are taken after the capital rise, except for
    document development and marketing expenses.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Reg CF is a medium-cost capital type that ranges from 11-18% (All-in). Regulation CF is
    generally cost-effective when compared to traditional private equity rounds or venture capital,
    which can involve much higher fees. Crowdfunding platforms charge fees (typically 3-7%), but
    these fees are relatively low compared to the costs of hiring a private equity firm or the
    significant fees associated with a full IPO. <b>NOTE NEED a dynamic response for the options for REG CF</b>The $5,000 - $9,999 budget would not be reasonable
    to cover platform fees (But the increased amounts can be paid on the back end), legal costs for
    filing, and marketing expenses to promote the campaign. With Regulation CF, there are legal
    compliance costs, including preparing the necessary offering documents and registration with the
    SEC, but these are typically much lower than the costs associated with more traditional funding
    methods, which align well with your budget (And they are on the back end).</p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Regulation CF offerings typically take 3-6 months to complete, depending on the complexity of
    the offering and the speed of SEC and platform approval.<b>NOTE NEED a dynamic response for the options for REG CF</b> Since you're looking 
    to raise funds in {upfronttime}.
    this timeframe, Regulation CF is a reasonable choice as it allows for quicker access to capital
    compared to traditional methods like venture capital or a private equity round.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)