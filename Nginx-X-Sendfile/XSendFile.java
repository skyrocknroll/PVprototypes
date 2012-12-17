package com.canvera.pvss;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class XSendFile
 */
@WebServlet("/")
public class XSendFile extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public XSendFile() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		PrintWriter out = response.getWriter();
		
		String requestURL = request.getRequestURI();
		System.out.println(requestURL);
		
		response.setHeader("X-Accel-Redirect", requestURL);
//		Random ra = new Random();
//		int x = ra.nextInt();
//		if (x%3 == 0)
//		response.setHeader("X-Accel-Redirect", "/lookup/127.0.0.1:90/500px/Rose.jpg");
//		else if (x%3 == 1)
//			response.setHeader("X-Accel-Redirect", "/lookup/127.0.0.1:90/500px/Garden.jpg");
//		else 
//		response.setHeader("X-Accel-Redirect", "/lookup/127.0.0.1:90/500px/Squirrel.jpg");
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}

