-- Sample num-1 | Using normal SQL--
SELECT DISTINCT part,
       assembly_step
FROM parts_assembly
where finish_date IS NULL;