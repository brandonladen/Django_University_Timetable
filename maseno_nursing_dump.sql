-- Drop existing tables if they exist
DROP TABLE IF EXISTS timetabling_unit;
DROP TABLE IF EXISTS timetabling_course;
DROP TABLE IF EXISTS timetabling_department;

-- Create table for departments
CREATE TABLE timetabling_department (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  school_id BIGINT NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for courses
CREATE TABLE timetabling_course (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  code VARCHAR(10) NOT NULL UNIQUE,
  department_id BIGINT NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for units
CREATE TABLE timetabling_unit (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  code VARCHAR(100) NOT NULL UNIQUE,
  course_id BIGINT NOT NULL,
  PRIMARY KEY (id)
);

-- Insert data into timetabling_department
INSERT INTO timetabling_department (id, name, school_id)
VALUES
  (1, 'Department of Medical Surgical Nursing', 1),
  (2, 'Department of Community Health Nursing', 1),
  (3, 'Department of Midwifery', 1),
  (4, 'Department of Nursing Education, Leadership and Research', 1);

-- Insert data into timetabling_course
INSERT INTO timetabling_course (id, name, code, department_id)
VALUES
  (1, 'Bachelor of Science in Nursing with IT', 'NUR101', 1),
  (2, 'Bachelor of Science in Nursing with IT', 'NUR102', 2),
  (3, 'Bachelor of Science in Nursing with IT', 'NUR103', 3),
  (4, 'Bachelor of Science in Nursing with IT', 'NUR104', 4);

-- Insert data into timetabling_unit

-- Department of Medical Surgical Nursing (course_id = 1)
-- Year 1
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (1, 'Foundations of Nursing', 'NSC103', 1),
  (2, 'Basic Life Saving Skills', 'NSC109', 1);
  
-- Year 2
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (3, 'Health Assessment', 'NSC205', 1),
  (4, 'Medical Surgical Nursing I Theory', 'NSC209T', 1),
  (5, 'Medical Surgical Nursing I Practical', 'NSC209P', 1);
  
-- Year 3
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (6, 'Medical Surgical Nursing II Theory and Practical', 'NSC300', 1),
  (7, 'Pediatric Nursing Theory and Practical', 'NSC301', 1),
  (8, 'Critical Care and Renal Nursing Theory and Practical', 'NSC309', 1),
  (9, 'Trauma & Emergency Nursing Theory and Practical', 'NSC310', 1);
  
-- Year 4
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (10, 'Palliative Care Nursing', 'NSC404', 1),
  (11, 'Perio-Operative Nursing', 'NSC406', 1),
  (12, 'Special Senses Nursing', 'NSC407', 1),
  (13, 'Geriatric Nursing', 'NSC410', 1);

-- Department of Community Health Nursing (course_id = 2)
-- Year 1
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (14, 'Psychology', 'NSC104', 2),
  (15, 'Community Health Nursing I', 'NSC106', 2),
  (16, 'Medical Sociology and Anthropology', 'NSC108', 2);
  
-- Year 2
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (17, 'Nutrition and Health', 'NSC207', 2),
  (18, 'Community Health Nursing II', 'NSC210', 2);
  
-- Year 3
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (19, 'Forensic Nursing', 'NSC306', 2);
  
-- Year 4
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (20, 'Mental Health and Psychiatric Nursing', 'NSC402', 2),
  (21, 'Community Health Nursing III', 'NSC411', 2);

-- Department of Midwifery (course_id = 3)
-- Year 2
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (22, 'Midwifery I', 'NSC208', 3);
  
-- Year 3
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (23, 'Midwifery II', 'NSC304', 3),
  (24, 'Gynaecology Nursing', 'NSC305', 3),
  (25, 'Gender, Sexual and Reproductive Health', 'NSC308', 3);
  
-- Year 4
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (26, 'Midwifery III', 'NSC401', 3);

-- Department of Nursing Education, Leadership and Research (course_id = 4)
-- Year 2
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (27, 'Human Communication Skills and Counseling', 'NSC204', 4);
  
-- Year 3
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (28, 'Research Methodology', 'NSC302', 4),
  (29, 'Biostatistics', 'NSC307', 4),
  (30, 'Nursing Electives', 'MNS310', 4),
  (31, 'Health Information Systems', 'HIT301', 4),
  (32, 'Electronic Commerce in Health', 'HIT302', 4),
  (33, 'Multimedia And Graphics in Health', 'HIT303', 4),
  (34, 'Data Management in Health', 'HIT304', 4);
  
-- Year 4
INSERT INTO timetabling_unit (id, name, code, course_id) VALUES 
  (35, 'Nursing Electives', 'NSC400', 4),
  (36, 'Nursing Education', 'NSC403', 4),
  (37, 'Nursing Leadership and Administration', 'NSC405', 4),
  (38, 'Research Project', 'NSC408', 4),
  (39, 'Teaching Practicum', 'NSC409', 4),
  (40, 'Health Information Systems Analysis and Design', 'HIT402', 4),
  (41, 'Social And Professional Issues In Health IT', 'HIT401', 4),
  (42, 'Information Assurance and Security in the Health IT Environment', 'HIT403', 4),
  (43, 'Special Topics In Health ICTs', 'HIT404', 4);
