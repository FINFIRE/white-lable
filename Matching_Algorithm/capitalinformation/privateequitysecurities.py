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

def privateequitysecurities(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Capital Market: Private Equity Securities</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Private equity securities are ideal for companies raising equity capital in amounts ranging from $1 million to over $100 million dollars in a given 12-month period. They are designed to provide businesses with significant capital in exchange for ownership stakes, with investors often becoming actively involved in management and strategic decisions. {n} fits that definition. Private equity has been a reliable tool for companies looking to expand and grow. For example, in 2023, private equity investments globally reached over $800 billion. In 2022, private equity firms made investments totaling approximately $650 billion across various industries. The total valuation of all private equity-backed companies raising in 2023 was estimated at $2.5 trillion. On average, each private equity raises in 2023 had a valuation of $150 million to $2 billion. However, as with any investment, private equity securities come with risks. These include dilution of control, the pressure to meet investor expectations for high returns, and the possibility of conflicts between investors and company management.  There are 15 types of Private Equity Securities that we can match you with: 1) Accredited Investors, 2) Angel Investors, 3) Broker Dealer (3,378), 4) Convertible Notes, 5) Family & Friends, 6) Family Offices, 7) High Net Worth Individuals, 8) Private Placement Memorandum, 9) Regulation A, 10) Regulation CF Title III, 11) Regulation D 504, 12) Regulation D 506(b), 13) Regulation D 506(c), 14) Rule 144, 15) Simple Agreement Future Equity. We will select the most appropriate type of Private Equity Security as per your business need.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Private equity securities are ownership interests in private companies that are not listed on public stock exchanges. These securities typically involve the direct investment of capital by private equity firms or accredited investors in exchange for equity—often in the form of common or preferred stock. Private equity investments are usually made in established businesses seeking capital for expansion, restructuring, or strategic acquisitions. Because these securities are illiquid and involve longer holding periods (often 5–10 years), they are generally considered higher risk but offer the potential for significant returns upon exit through a sale, merger, or IPO. (Chen, 2024)
    <br>
    <br>2. Private equity securities come in several forms, each tailored to different stages of a company’s growth and investor risk preferences. Common types include leveraged buyouts (LBOs), growth equity, venture capital, distressed or turnaround investments, and mezzanine financing. Leveraged buyouts involve acquiring a mature company using a combination of debt and equity, typically to improve operations and later sell for a profit. Growth equity provides capital to established companies seeking to expand without taking on full control. Venture capital focuses on early-stage startups with high growth potential in exchange for equity stakes. Distressed or turnaround investments target underperforming companies that can be restructured or revived for gain. Mezzanine financing is a hybrid of debt and equity—investors receive interest payments but may convert the loan to equity if not repaid. Each type of security varies in risk, return expectations, and involvement in the company’s operations. (HBS, 2021)
    <br>
    <br>3. Private equity securities have a long and evolving history, dating back to the early 20th century, but the modern private equity industry began to take shape in the post-World War II era. In 1946, two of the earliest venture capital firms—American Research and Development Corporation (ARDC) and J.H. Whitney & Company—were founded, aiming to invest in startups and emerging businesses. The industry saw steady growth through the 1960s and 1970s but truly accelerated in the 1980s with the rise of leveraged buyouts (LBOs), fueled by deregulation, financial innovation, and access to cheap debt. Firms like KKR and The Blackstone Group became household names as they executed multi-billion-dollar acquisitions. In the 2000s, private equity matured into a major asset class, attracting institutional capital and expanding globally. Today, private equity securities encompass a wide range of strategies—from venture capital to distressed investing—and play a critical role in funding innovation and restructuring businesses across sectors. (History of Private Equity and Venture Capital, n.d.)
    <br>
    <br>4. Private equity securities come with several risks for companies seeking capital. One of the main risks is loss of control, as private equity firms often demand significant influence over management decisions, board representation, or even majority ownership. This can alter the strategic direction of the company or lead to conflicts between founders and investors. Additionally, private equity funding often comes with performance expectations and timelines—companies may face pressure to scale quickly or hit aggressive growth targets, potentially leading to risky business decisions. There’s also the risk of dilution of ownership, as equity is exchanged for capital. Lastly, if the partnership fails to yield expected results, companies may struggle with limited exit options, especially in industries with long development cycles or low market liquidity. While private equity can offer substantial growth capital, it requires careful consideration of both financial and strategic trade-offs. (Growth Equity Interview Guide, 2025)
    <br>
    <br>5. To raise capital through private equity securities, a company must meet certain requirements. First, it must have a compelling business model with strong growth potential, as private equity investors seek companies that can deliver high returns. The company needs to have a clear financial history and solid management team to instill investor confidence. A well-prepared business plan that outlines the company’s strategy, market opportunities, and financial projections is essential. Additionally, the company must have a registered legal structure, such as a corporation or LLC, to issue equity securities. It is also important to have a strong track record of financial performance or a compelling growth trajectory, as private equity firms often prefer businesses that are beyond the startup stage but still require capital for scaling. Legal and regulatory compliance, such as adherence to securities laws, is critical, and companies will need to work with legal and financial advisors to navigate these requirements. The company must also be prepared to give up some level of control, as private equity investors typically demand significant influence over company decisions in exchange for their capital. (Padua, 2021)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Chen, J. (2024, April 10). Private equity explained with examples and ways to invest. Investopedia. <a href="https://www.investopedia.com/terms/p/privateequity.asp">https://www.investopedia.com/terms/p/privateequity.asp</a>
<br>
    <br>3 Key types of private equity | HBS Online. (2021, July 13). Business Insights Blog. <a href="https://online.hbs.edu/blog/post/types-of-private-equity?">https://online.hbs.edu/blog/post/types-of-private-equity?</a>
<br>
    <br>History of Private Equity and Venture Capital/origins of Modern Private Equity? | History Private Equity Venture Capital Origins Modern Private Equity? N.d. <a href="https://www.liquisearch.com/history_of_private_equity_and_venture_capital/origins_of_modern_private_equity?">https://www.liquisearch.com/history_of_private_equity_and_venture_capital/origins_of_modern_private_equity?</a>
<br>
    <br>Growth Equity Interview Guide. (2025, March 13). Private Equity Risk Management: Strategies for handling risks. <a href="https://growthequityinterviewguide.com/private-equity/private-equity-operations/private-equity-risk-management?">https://growthequityinterviewguide.com/private-equity/private-equity-operations/private-equity-risk-management?</a>
<br>
    <br>Padua, A. (2021, February 2). Raising capital through a private placement of equity securities. Padua Law Firm. <a href="https://www.padualaw.com/corporate-law/raising-capital-private-placement-equity-securities/">https://www.padualaw.com/corporate-law/raising-capital-private-placement-equity-securities/</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Entity Structure: The company must be a legally registered entity (LLC, corporation, etc.).
    <br>• Accredited Investors: Securities must be sold primarily to accredited investors unless using specific exemptions.
    <br>• Exemptions: The company must comply with exemptions like Regulation D (e.g., Rule 506(b) or 506(c)).
    <br>• PPM: A Private Placement Memorandum must be prepared to outline investment terms.
    <br>• Form D Filing: Must file Form D with the SEC after the first sale of securities.
    <br>• State Compliance: Must comply with state securities laws (Blue Sky laws).
    <br>• No Public Offering: The offering must not be a public offering under SEC rules.
    <br>• Investor Limits: There are restrictions on the number of investors and solicitation methods.
    <br>• Disclosure: Financial statements and risk disclosures must be provided to investors.
    <br>• Advisors: Engage legal and financial advisors for compliance.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Entity Structure: The company must be a legally registered entity (LLC, corporation, etc.).
    <br>• Accredited Investors: Securities must be sold primarily to accredited investors unless using specific exemptions.
    <br>• Exemptions: The company must comply with exemptions like Regulation D (e.g., Rule 506(b) or 506(c)).
    <br>• PPM: A Private Placement Memorandum must be prepared to outline investment terms.
    <br>• Form D Filing: Must file Form D with the SEC after the first sale of securities.
    <br>• State Compliance: Must comply with state securities laws (Blue Sky laws).
    <br>• No Public Offering: The offering must not be a public offering under SEC rules.
    <br>• Investor Limits: There are restrictions on the number of investors and solicitation methods.
    <br>• Disclosure: Financial statements and risk disclosures must be provided to investors.
    <br>• Advisors: Engage legal and financial advisors for compliance.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesfaq(request):
    introduction = mark_safe("""
    <p><b><u>FAQs<u/></b></p>                        
                             
    <p><b><u>1. What are private equity securities?</u></b><br>
    • Answer: Private equity securities represent ownership in a privately held company. They can include common stock, preferred shares, convertible notes, and other equity instruments not traded on public markets.
    </p>
                             
    <p><b><u>2. Who typically invests in private equity?</u></b><br>
    • Answer: Institutional investors (like pension funds, endowments, and insurance companies), high-net-worth individuals, family offices, and private equity firms are the most common investors in this space.
    </p>
                             
    <p><b><u>3. When is the right time to raise private equity?</u></b><br>
    • Answer: Typically, during growth stages (Series B and beyond) when your business has strong revenue traction, product-market fit, and a clear path to scale or exit.
    </p>
                             
    <p><b><u>4. What types of private equity securities are there?</u></b><br>
    • Answer: The most common types are common stock, preferred equity, convertible preferred stock, and warrants. Each has different rights, risks, and levels of investor control.
    </p>
                             
    <p><b><u>5. How much control do private equity investors have?</u></b><br>
    • Answer: PE investors usually get board seats, veto rights, or protective provisions. The level of control depends on the amount of capital invested and the terms negotiated.
    </p>
                             
    <p><b><u>6. What are the benefits of private equity?</u></b><br>
    • Answer: Large infusions of capital, strategic guidance, access to networks, and a long-term partnership for growth and scaling.
    </p>
                             
    <p><b><u>7. What are the risks for a company raising private equity?</u></b><br>
    • Answer: Key risks include ownership dilution, loss of strategic independence, misalignment of goals, and pressure to exit (via IPO or sale).
    </p>
                             
    <p><b><u>8. How long does a private equity raise take?</u></b><br>
    • Answer: On average, 3–9 months, depending on investor interest, company readiness, legal diligence, and complexity of the deal.
    </p>
                             
    <p><b><u>9. Do I need audited financials to raise private equity?</u></b><br>
    • Answer: While not always mandatory, audited or GAAP-compliant financials significantly improve investor confidence and are often required for later-stage rounds.</p>
                             
    <p><b><u>10. Can startups raise private equity?</u></b><br>
    • Answer: Early-stage startups usually pursue venture capital, not traditional private equity. PE is better suited for mature startups, scale-ups, or established private companies.
    </p>                                            
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiestwelve(request):
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
        'Minimum $0 - Maximum $499' : 'The available capital would be insufficient to cover intermediary fees, offering documentation, and legal expenses prior to the capital raise.',
        'Minimum $500 - Maximum $999' : 'The available capital would be insufficient to cover intermediary fees, offering documentation, and legal expenses prior to the capital raise.',
        'Minimum $1000 - Maximum $2499' : 'The available capital would be insufficient to cover intermediary fees, offering documentation, and legal expenses prior to the capital raise.',
        'Minimum $2500 - Maximum $4999' : 'it issuer may need to streamline the transaction structure or target smaller private equity investors to maintain budgetary constraints. Engaging outside counsel or fixed-fee legal providers could optimize cost management in this process.',
        'Minimum $5000 - Maximum $9999' : 'it issuer may need to streamline the transaction structure or target smaller private equity investors to maintain budgetary constraints. Engaging outside counsel or fixed-fee legal providers could optimize cost management in this process.',
        'Minimum $10000 - Maximum $24999' : 'it issuer may need to streamline the transaction structure or target smaller private equity investors to maintain budgetary constraints. Engaging outside counsel or fixed-fee legal providers could optimize cost management in this process.',
        'Minimum $25000 - Maximum $49999' : 'The allocated capital will typically cover all intermediary fees and associated funding expenses, with only exceptional circumstances requiring additional budgetary provisions.',
        'More than $50000+' : 'The allocated capital will typically cover all intermediary fees and associated funding expenses, with only exceptional circumstances requiring additional budgetary provisions.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'While completing the entire process within a 1 day to 1 week timeframe presents significant challenges, execution may be feasible if the majority of offering documents are substantially prepared in advance.',
        '1 Week to 2 Week' : 'While completing the entire process within a 1-2 week timeframe presents significant challenges, execution may be feasible if the majority of offering documents are substantially prepared in advance.',
        '2 Weeks to 4 Weeks' : 'However, the timeline can be substantially compressed through: (1) comprehensive preparatory work, (2) a fully organized virtual data room, and (3) targeted outreach to pre-aligned investors with demonstrated sector interest.',
        '1 Month to 2 Months' : 'However, the timeline can be substantially compressed through: (1) comprehensive preparatory work, (2) a fully organized virtual data room, and (3) targeted outreach to pre-aligned investors with demonstrated sector interest.',
        '2 Months to 3 Months' : 'We can anticipate completing the process within a 2-3 month timeframe with high confidence, assuming substantial completion of key prerequisites including due diligence materials, investor documentation, and regulatory filings.',
        '3 Months to 6 Months' : 'We can anticipate completing the process within a 2-3 month timeframe with high confidence, assuming substantial completion of key prerequisites including due diligence materials, investor documentation, and regulatory filings.',
        '6 Months to 12 Months' : '6 months to 12 months provides sufficient time to execute the full capital raise, even without pre-existing marketing materials, allowing for the development of institutional-quality documentation, systematic investor outreach, and thorough due diligence. This extended timeline also creates capacity to evaluate subsequent funding tranches concurrently with the final stages of the primary offering.',
        'More than 1 year' : 'A 12+ month horizon provides sufficient time to execute the full capital raise, even without pre-existing marketing materials, allowing for the development of institutional-quality documentation, systematic investor outreach, and thorough due diligence. This extended timeline also creates capacity to evaluate subsequent funding tranches concurrently with the final stages of the primary offering.',             
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
    Private Equity Securities</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As {n} moves into a {stage} stage, utilizing private equity securities can provide a more structured and strategic approach to raising capital. Private equity involves immediate ownership exchange, which can be beneficial when the company has clearer metrics for valuation. This is ideal for companies that have demonstrated traction and are ready to bring on strategic investors who can add more than capital—such as industry expertise and operational support.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Private equity investments are best suited for {entity}, as they allow for the issuance of preferred shares and a structured cap table—both of which are common in private equity deals. {n}’s corporate structure is a good match, especially if the company is considering follow-on rounds or an eventual exit strategy such as acquisition or IPO.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} in pre-capital already raised, {n} is in a strong position to attract private equity investors who are typically more risk-averse than angel investors or SAFE participants. These investors will expect a formal valuation and due diligence process, but in return may offer larger checks, deeper involvement, and long-term strategic guidance.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Given the existing capital foundation, moving toward private equity securities in future rounds allows {n} to access institutional or high-net-worth investors who prefer equity stakes with voting rights, board seats, and liquidation preferences. This shift indicates maturity and confidence in the company’s valuation and trajectory.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Raising {raisegoal} through private equity will require a defined valuation and investor agreement. While it involves more complexity than a SAFE, it brings structure, strategic alignment, and long-term accountability. This is a suitable amount for private equity if tied to a clear use-of-funds plan and growth milestones.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Private equity is common during Series B, C, and later rounds. At these points, businesses are scaling quickly and may need capital for strategic expansion, not just survival. Institutional investors look for sustainable growth and measurable ROI.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Private equity capital can be structured into tranches tied to performance milestones, offering a balance between investor confidence and founder flexibility. This staged approach allows XYZ company to unlock additional capital as it hits key growth benchmarks, reducing dilution risk and aligning incentives.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Private equity funds are used for high-growth initiatives: geographic expansion, product scaling, strategic hires, infrastructure upgrades, or acquisitions. Clear plans for capital deployment aligned with growth projections are essential for investor confidence.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Private equity investors generally expect a lower risk profile, so {n} must demonstrate traction, revenue potential, and scalability. While this capital comes with oversight and control provisions, it offers access to more substantial funding and long-term partners.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The cost of private equity is high due to equity dilution. PE firms typically seek high returns (3x–5x or more) over several years. While there’s no repayment obligation like debt, equity holders expect significant upside and influence over company direction.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Legal, accounting, and due diligence expenses for private equity can range from $25,000 to $150,000, depending on complexity. If {n} has a {upfrontcost}, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Private equity fundraising generally takes 1–6 months or more due to valuation negotiations, due diligence, and investor vetting. {timeanalysis}</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,timeanalysis=timeanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)